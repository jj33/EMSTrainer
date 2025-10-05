#!/usr/bin/env python3
import os, re, sys, argparse

CHECKBOX_RE = re.compile(r"^(?P<prefix>\s*(?:[-*+]|\d+\.)\s*)\[(?: |x|X)\]\s*", re.MULTILINE)
BARE_BOX_RE = re.compile(r"^(?P<prefix>\s*)\[(?: |x|X)\]\s*", re.MULTILINE)
OPEN_TAG_RE = re.compile(r"<(button|input|form|details|summary|select|option|dialog)(\s[^>]*)?>", re.IGNORECASE)
CLOSE_TAG_RE = re.compile(r"</(button|form|details|summary|select|option|dialog)>", re.IGNORECASE)
YAML_FRONT_RE = re.compile(r"\A---\s*\n(.*?\n)---\s*\n", re.DOTALL)

TEXT_EXTS = {'.txt', '.md', '.markdown', '.prompt'}

def lint_text(content: str) -> str:
    content = re.sub(YAML_FRONT_RE, '', content)
    content = re.sub(CHECKBOX_RE, r"• ", content)
    content = re.sub(BARE_BOX_RE, r"• ", content)
    content = re.sub(OPEN_TAG_RE, '', content)
    content = re.sub(CLOSE_TAG_RE, '', content)
    return content

def process_path(path: str, backup: bool, dry_run: bool):
    changed = 0
    scanned = 0
    modified_files = []
    for root, _, files in os.walk(path):
        for name in files:
            ext = os.path.splitext(name)[1].lower()
            if ext not in TEXT_EXTS:
                continue
            fp = os.path.join(root, name)
            try:
                with open(fp, 'r', encoding='utf-8') as f:
                    original = f.read()
            except Exception:
                continue
            scanned += 1
            updated = lint_text(original)
            if updated != original:
                changed += 1
                modified_files.append(fp)
                if not dry_run:
                    if backup:
                        with open(fp + ' .bak', 'w', encoding='utf-8') as fb:
                            fb.write(original)
                    with open(fp, 'w', encoding='utf-8') as fw:
                        fw.write(updated)
    return scanned, changed, modified_files

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('root', nargs='?', default='prompts', help='Root path to scan (default: prompts)')
    ap.add_argument('--backup', action='store_true', help='Write .bak backup files before modifying')
    ap.add_argument('--dry-run', action='store_true', help='Scan and report without modifying files')
    ap.add_argument('--exit-nonzero-on-changes', action='store_true', help='Exit code 2 if changes are detected')
    args = ap.parse_args()

    scanned, changed, files = process_path(args.root, backup=args.backup, dry_run=args.dry_run)

    print(f"Scanned files: {scanned}")
    print(f"Modified files: {changed}")
    if files:
        print("\nChanged:")
        for fp in files:
            print(" -", fp)

    if args.exit_nonzero_on_changes and changed > 0:
        sys.exit(2)
