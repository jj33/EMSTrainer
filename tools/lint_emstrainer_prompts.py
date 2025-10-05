#!/usr/bin/env python3
import os, sys
import argparse

def lint_file(path, backup=False):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content
    # Remove markdown checkboxes
    new_content = new_content.replace('- [ ]', '•').replace('- [x]', '•')
    # Remove interactive HTML tags
    for tag in ['<button', '<details', '<form', '<input', '<select', '<option', '<dialog']:
        while tag in new_content:
            start = new_content.find(tag)
            end = new_content.find('>', start)
            if end != -1:
                new_content = new_content[:start] + new_content[end+1:]
            else:
                break
    # Remove YAML front matter
    if new_content.startswith('---'):
        end_yaml = new_content.find('---', 3)
        if end_yaml != -1:
            new_content = new_content[end_yaml+3:]
    if new_content != content:
        if backup:
            with open(path + '.bak', 'w', encoding='utf-8') as f:
                f.write(content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', default='.')
    parser.add_argument('--backup', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--exit-nonzero-on-changes', action='store_true')
    args = parser.parse_args()

    changed = 0
    for dirpath, _, filenames in os.walk(args.root):
        for fn in filenames:
            if fn.lower().endswith(('.txt', '.md', '.markdown', '.prompt')):
                path = os.path.join(dirpath, fn)
                if lint_file(path, backup=args.backup) and not args.dry_run:
                    changed += 1
    if args.exit_nonzero_on_changes and changed > 0:
        sys.exit(2)

if __name__ == '__main__':
    main()
