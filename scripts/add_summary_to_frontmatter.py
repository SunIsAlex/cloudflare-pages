#!/usr/bin/env python3
import argparse
import os
import re
import textwrap

FRONTMATTER_DELIM = re.compile(r'^---\s*$', re.MULTILINE)
SUMMARY_KEY = re.compile(r'^\s*summary\s*:', re.MULTILINE)


def split_frontmatter(text):
    if not text.startswith('---'):
        return None, text
    matches = list(FRONTMATTER_DELIM.finditer(text))
    if len(matches) < 2:
        return None, text
    start = matches[0].end()
    end = matches[1].start()
    frontmatter = text[: end].strip('\n') + '\n'
    body = text[matches[1].end() :]
    return frontmatter, body


def clean_markdown(text):
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    text = re.sub(r'\{\{<[^>]+>\}\}', '', text)
    text = re.sub(r'\{\{[^}]+\}\}', '', text)
    text = re.sub(r'!\[[^\]]*\]\([^\)]*\)', '', text)
    text = re.sub(r'\[[^\]]*\]\([^\)]*\)', lambda m: m.group(0).split(']')[0].lstrip('['), text)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)
    text = re.sub(r'\$\$[\s\S]*?\$\$', '', text)
    text = re.sub(r'\$[^\$]+\$', '', text)
    text = re.sub(r'\\\([^\)]+\\\)', '', text)
    text = re.sub(r'\\\[[^\]]+\\\]', '', text)
    text = re.sub(r'\\[a-zA-Z]+', '', text)
    text = re.sub(r'#+\s*', '', text)
    text = re.sub(r'>\s*', '', text)
    text = re.sub(r'\|', ' ', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_paragraphs(body):
    body = clean_markdown(body)
    paragraphs = []
    for part in re.split(r'\n\s*\n', body):
        line = part.strip()
        if not line:
            continue
        if re.match(r'^(?:\d+\.|\*|\-|•|\+|=)\s+', line):
            continue
        if len(line) < 20:
            continue
        paragraphs.append(line)
    return paragraphs


def split_sentences(text):
    sentences = re.split(r'(?<=[。！？!?\.])\s+', text)
    return [s.strip() for s in sentences if s.strip()]


def extract_title(frontmatter):
    match = re.search(r'^\s*title\s*:\s*(.+)$', frontmatter, re.MULTILINE)
    if not match:
        return None
    title = match.group(1).strip()
    title = title.strip('"\'')
    return title


def generate_summary(body, title=None):
    paragraphs = extract_paragraphs(body)
    if not paragraphs:
        return None
    candidate = paragraphs[0]
    if len(paragraphs) > 1 and len(candidate) < 70:
        candidate = paragraphs[0] + ' ' + paragraphs[1]
    sentences = split_sentences(candidate)
    if len(sentences) >= 2:
        candidate = sentences[0]
        if len(candidate) < 80:
            candidate = candidate + ' ' + sentences[1]
    elif sentences:
        candidate = sentences[0]
    if title:
        title = title.strip('"\'')
        candidate = f'{title}：{candidate}'
    candidate = candidate.replace('  ', ' ').strip()
    return textwrap.shorten(candidate, width=140, placeholder='...')


def insert_summary(frontmatter, summary_text):
    lines = frontmatter.splitlines()
    if lines and lines[0].strip() == '---':
        lines = lines[1:]
    else:
        return frontmatter
    # remove trailing closing delimiter if present
    if lines and lines[-1].strip() == '---':
        lines = lines[:-1]
    # insert summary after title if title exists, else append at end
    insert_n = len(lines)
    for idx, line in enumerate(lines):
        if line.strip().startswith('title'):
            insert_n = idx + 1
            break
    summary_line = f'summary: "{summary_text.replace("\"", "\\\"")}"'
    lines.insert(insert_n, summary_line)
    return '---\n' + '\n'.join(lines) + '\n---\n'


def process_file(path, dry_run=False):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    frontmatter, body = split_frontmatter(text)
    if frontmatter is None:
        return False, 'no frontmatter'
    if SUMMARY_KEY.search(frontmatter):
        return False, 'summary exists'
    title = extract_title(frontmatter)
    summary = generate_summary(body, title=title)
    if not summary:
        return False, 'no summary generated'
    new_frontmatter = insert_summary(frontmatter, summary)
    if new_frontmatter == frontmatter:
        return False, 'no changes'
    if not dry_run:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_frontmatter)
            f.write(body.lstrip('\n'))
    return True, summary


def walk_and_process(root, dry_run=False):
    processed = []
    skipped = []
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if not name.lower().endswith('.md'):
                continue
            path = os.path.join(dirpath, name)
            ok, info = process_file(path, dry_run=dry_run)
            if ok:
                processed.append((path, info))
            else:
                skipped.append((path, info))
    return processed, skipped


def main():
    parser = argparse.ArgumentParser(description='Add missing summary fields to markdown frontmatter')
    parser.add_argument('root', nargs='?', default='content/posts', help='Root folder to scan')
    parser.add_argument('--dry-run', action='store_true', help='Do not modify files')
    args = parser.parse_args()
    processed, skipped = walk_and_process(args.root, dry_run=args.dry_run)
    print(f'Processed {len(processed)} files:')
    for path, summary in processed:
        print(f'  + {path}')
        print(f'    summary={summary}')
    print(f'Skipped {len(skipped)} files:')
    for path, reason in skipped:
        print(f'  - {path} ({reason})')


if __name__ == '__main__':
    main()
