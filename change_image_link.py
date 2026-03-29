import os
import re
import shutil
import argparse
from pathlib import Path

# ------------------- 配置区 -------------------
IMAGES_DIR_IN_STATIC = "static/images"       # 图片实际存储的位置
CONTENT_DIR = "content"
DRY_RUN = False
MOVE_INSTEAD_OF_COPY = False
BACKUP_MD = True

IMAGE_PATTERNS = [
    re.compile(r'!\[([^\]]*)\]\((/images/[^)]+)\)'),
    re.compile(r'src=["\'](/images/[^"\']+)["\']'),
    re.compile(r'["\'](/images/[^"\']+\.(?:jpg|jpeg|png|gif|webp|avif|svg))["\']', re.IGNORECASE),
]

def safe_relative(path: Path, base: Path = None):
    """安全地显示相对路径，避免 relative_to 报错"""
    if base is None:
        base = Path.cwd()
    try:
        return path.relative_to(base)
    except ValueError:
        return path

def get_bundle_name(md_path: Path) -> str:
    return md_path.stem

def find_images_in_md(content: str) -> list:
    images = []
    for pattern in IMAGE_PATTERNS:
        for match in pattern.finditer(content):
            img_path = match.group(2) if len(match.groups()) >= 2 else match.group(1)
            if img_path.startswith('/images/'):
                rel_name = img_path.replace('/images/', '', 1).lstrip('/')
                images.append((img_path, rel_name))
    return list(set(images))

def process_markdown_file(md_path: Path, project_root: Path):
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        images = find_images_in_md(content)
        if not images:
            return

        bundle_dir = md_path.parent / get_bundle_name(md_path)
        
        print(f"\n处理: {safe_relative(md_path, project_root)}")
        print(f"  → 创建 Bundle: {safe_relative(bundle_dir, project_root)}")

        if not DRY_RUN:
            bundle_dir.mkdir(parents=True, exist_ok=True)

        processed_images = []
        for full_url_path, rel_name in images:
            src_img = Path(IMAGES_DIR_IN_STATIC) / rel_name
            if not src_img.exists():
                print(f"  ⚠️  图片未找到: {src_img}")
                continue

            dest_img = bundle_dir / src_img.name
            if not DRY_RUN:
                if MOVE_INSTEAD_OF_COPY:
                    shutil.move(src_img, dest_img)
                else:
                    shutil.copy2(src_img, dest_img)

            processed_images.append((full_url_path, src_img.name))
            print(f"  ✓ 图片: {src_img.name}  →  {bundle_dir.name}/")

        # 修改路径
        new_content = content
        for old_path, new_name in processed_images:
            new_content = new_content.replace(old_path, new_name)

        index_md = bundle_dir / "index.md"
        if not DRY_RUN:
            if BACKUP_MD:
                backup = md_path.with_suffix('.md.bak')
                shutil.copy2(md_path, backup)
                print(f"  ✓ 已备份 → {safe_relative(backup, project_root)}")

            with open(index_md, 'w', encoding='utf-8') as f:
                f.write(new_content)

            if md_path.exists() and md_path != index_md:
                md_path.unlink()
                print(f"  ✓ 已删除原文件 {md_path.name}")

        print(f"  ✓ 完成")
        
    except Exception as e:
        print(f"  ❌ 处理失败 {safe_relative(md_path, project_root)}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Hugo /images → Page Bundle 迁移脚本")
    parser.add_argument("--dry-run", action="store_true", help="只预览")
    parser.add_argument("--move", action="store_true", help="移动图片而非复制")
    args = parser.parse_args()

    global DRY_RUN, MOVE_INSTEAD_OF_COPY
    DRY_RUN = args.dry_run
    MOVE_INSTEAD_OF_COPY = args.move

    project_root = Path.cwd()
    print(f"当前工作目录: {project_root}")
    print(f"static/images 路径: {project_root / IMAGES_DIR_IN_STATIC}")

    if not (project_root / CONTENT_DIR).exists():
        print(f"错误：未找到 {CONTENT_DIR} 目录！请在 Hugo 项目根目录运行脚本。")
        return

    print("=== 开始迁移 /images → Page Bundle ===\n")

    md_files = list((project_root / CONTENT_DIR).rglob("*.md"))
    print(f"共找到 {len(md_files)} 个 .md 文件\n")

    for md_file in md_files:
        if md_file.name == "index.md":
            continue
        process_markdown_file(md_file, project_root)

    print("\n=== 迁移结束 ===")
    if DRY_RUN:
        print("这是干运行模式，请去掉 --dry-run 后再正式执行。")

if __name__ == "__main__":
    main()
