#!/usr/bin/env python3

"""
Minimal smoke test for 'make exports'.
Creates demo MD and CSV files under exports/demo.
Replace with real export logic when ready.

Usage:
    python3 tools/export_smoke_test.py
"""
from __future__ import print_function
import csv
import datetime as dt
from pathlib import Path


def main():
    out_dir = Path('exports/demo')
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = [
        {"id": 1, "name": "Sample Scenario A", "level": "EMT"},
        {"id": 2, "name": "Sample Scenario B", "level": "Paramedic"},
    ]

    csv_path = out_dir / 'demo_acs_export.csv'
    with csv_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'name', 'level'])
        writer.writeheader()
        writer.writerows(rows)

    md_path = out_dir / 'demo_acs_export.md'
    now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    md_lines = [
        '# Demo ACS Export',
        '',
        f'_Generated: {now}_',
        '',
        '## Scenarios',
        '',
    ]
    for r in rows:
        md_lines.append(f"- ID {r['id']} - {r['name']} ({r['level']})")
    md_text = '\n'.join(md_lines) + '\n'
    md_path.write_text(md_text, encoding='utf-8')

    print('Wrote:', csv_path)
    print('Wrote:', md_path)


if __name__ == '__main__':
    main()
