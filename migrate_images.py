#!/usr/bin/env python3
"""
migrate_images.py
-----------------
扫描 content/posts 下所有 .md 文件，将 front matter 和 markdown 正文中
指定域名的图片 URL 下载到 static/images/，并将 .md 文件中的链接替换为
本地路径 /images/<filename>。

目标域名（TARGET_DOMAINS）：
  - cdn.sunisalex.org
  - free.picui.cn

支持的 markdown 图片格式：
  ![alt](URL)
  ![alt](URL "title")
  ![alt](URL 'title')

用法：
  python3 migrate_images.py [--dry-run] [--root 项目根目录]

  --dry-run   只打印将要做的操作，不真正修改文件或下载图片
  --root      Hugo 项目根目录，默认为当前目录
"""

import argparse
import hashlib
import re
import sys
import urllib.parse
from pathlib import Path

import requests

# ── 配置 ────────────────────────────────────────────────────────────────────

TARGET_DOMAINS = {
    "cdn.sunisalex.org",
    "free.picui.cn",
}

_DOMAIN_PATTERN = r"https?://(?:" + "|".join(re.escape(d) for d in TARGET_DOMAINS) + r")[^\s)\"'<>]+"

# 匹配 front matter 中的图片字段，支持带引号或不带引号
# image: "URL"  /  image: 'URL'  /  image: URL
FRONT_MATTER_IMAGE_RE = re.compile(
    r'(image:\s*["\']?)(' + _DOMAIN_PATTERN + r')(["\']?)',
    re.IGNORECASE,
)

# 匹配 markdown 图片语法，支持带 title 或不带 title：
#   ![alt](URL)
#   ![alt](URL "title")
#   ![alt](URL 'title')
# 只替换 URL 部分（group 2），title 和括号保留不动
MARKDOWN_IMAGE_RE = re.compile(
    r'(!\[[^\]]*\]\()'           # group1: ![alt](
    r'(' + _DOMAIN_PATTERN + r')'  # group2: URL（目标域名）
    r'((?:\s+["\'][^"\']*["\'])?\))',  # group3: 可选 title + 闭合括号
    re.IGNORECASE,
)

TIMEOUT = 30  # 下载超时（秒）

# ── 工具函数 ─────────────────────────────────────────────────────────────────


def url_to_filename(url: str) -> str:
    """将 URL 转换为本地文件名，取路径最后一段；无文件名时用 URL 哈希。"""
    parsed = urllib.parse.urlparse(url)
    basename = Path(parsed.path).name
    if not basename:
        basename = hashlib.md5(url.encode()).hexdigest()[:12]
    return basename


def unique_filename(target_dir: Path, preferred_name: str, url: str) -> str:
    """
    确保文件名在 target_dir 下唯一。
    若同名文件已存在（来自不同 URL），插入 URL 短哈希加以区分。
    """
    if not (target_dir / preferred_name).exists():
        return preferred_name
    stem = Path(preferred_name).stem
    suffix = Path(preferred_name).suffix
    short_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    return f"{stem}_{short_hash}{suffix}"


def download_image(url: str, target_dir: Path, dry_run: bool) -> str | None:
    """
    下载图片到 target_dir，返回本地文件名（不含目录），失败返回 None。
    """
    preferred = url_to_filename(url)
    filename = unique_filename(target_dir, preferred, url)
    dest = target_dir / filename

    if dest.exists():
        print(f"  [已存在] {filename}  <- {url}")
        return filename

    if dry_run:
        print(f"  [DRY-RUN 下载] {url}  ->  static/images/{filename}")
        return filename

    print(f"  [下载] {url}")
    try:
        resp = requests.get(url, timeout=TIMEOUT, stream=True)
        resp.raise_for_status()
        target_dir.mkdir(parents=True, exist_ok=True)
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"         -> static/images/{filename}")
        return filename
    except Exception as e:
        print(f"  [错误] 下载失败：{url}\n         原因：{e}", file=sys.stderr)
        return None


def collect_matches(text: str) -> list[tuple[int, int, str]]:
    """
    在 text 中找出所有需要替换的 URL 及其位置，返回 (start, end, url) 列表。
    """
    matches: list[tuple[int, int, str]] = []

    for m in FRONT_MATTER_IMAGE_RE.finditer(text):
        matches.append((m.start(2), m.end(2), m.group(2)))

    for m in MARKDOWN_IMAGE_RE.finditer(text):
        matches.append((m.start(2), m.end(2), m.group(2)))

    return matches


def process_file(md_path: Path, images_dir: Path, dry_run: bool) -> int:
    """处理单个 .md 文件，返回替换次数。"""
    original = md_path.read_text(encoding="utf-8")
    updated = original

    # 第一遍：收集所有 URL，去重下载
    initial_matches = collect_matches(updated)
    if not initial_matches:
        return 0

    url_to_local: dict[str, str | None] = {}
    for _, _, url in initial_matches:
        if url not in url_to_local:
            url_to_local[url] = download_image(url, images_dir, dry_run)

    # 第二遍：重新收集位置（文件内容未变，位置稳定），从后往前替换
    all_matches = collect_matches(updated)
    all_matches.sort(key=lambda x: x[0], reverse=True)

    replacements = 0
    for start, end, url in all_matches:
        local_name = url_to_local.get(url)
        if not local_name:
            continue
        local_path = f"/images/{local_name}"
        if dry_run:
            print(f"  [DRY-RUN 替换] {url}  ->  {local_path}")
        updated = updated[:start] + local_path + updated[end:]
        replacements += 1

    if replacements > 0 and not dry_run:
        md_path.write_text(updated, encoding="utf-8")

    return replacements


# ── 主程序 ───────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="将 content/posts 下 .md 文件中指定域名的图片下载并本地化"
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Hugo 项目根目录（默认：当前目录）",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只打印操作，不实际下载或修改文件",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    posts_dir = root / "content" / "posts"   # 已修正为 posts
    images_dir = root / "static" / "images"

    if not posts_dir.exists():
        print(f"[错误] 目录不存在：{posts_dir}", file=sys.stderr)
        sys.exit(1)

    if not args.dry_run:
        images_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(posts_dir.rglob("*.md"))
    print(f"共找到 {len(md_files)} 个 .md 文件（在 {posts_dir}）\n")

    total_replacements = 0
    for md_file in md_files:
        rel = md_file.relative_to(root)
        count = process_file(md_file, images_dir, args.dry_run)
        if count:
            total_replacements += count
            print(f"[OK] {rel}  [{count} 处替换]\n")

    print(f"共替换 {total_replacements} 处。{'（DRY-RUN 模式，文件未修改）' if args.dry_run else ''}")


if __name__ == "__main__":
    main()
