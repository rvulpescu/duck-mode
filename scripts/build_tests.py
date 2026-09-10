#!/usr/bin/env python3
"""Generate validated behavioral case data from SPEC.md; does not run models."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def cases_from_spec():
    spec = (ROOT / 'SPEC.md').read_text()
    start, end = '<!-- DUCK_TESTS_START -->', '<!-- DUCK_TESTS_END -->'
    if spec.count(start) != 1 or spec.count(end) != 1:
        raise ValueError('Expected one canonical test block')
    block = spec.split(start)[1].split(end)[0].strip()
    if not block.startswith('```json\n') or not block.endswith('\n```'):
        raise ValueError('Expected fenced JSON cases')
    cases = json.loads(block[len('```json\n'):-len('\n```')])
    ids, coverage = set(), Counter()
    valid = {f'D{i:02}' for i in range(1, 25)}
    for case in cases:
        if case['id'] in ids or not re.fullmatch(r'[a-z0-9-]+', case['id']):
            raise ValueError('Invalid or duplicate case ID')
        ids.add(case['id'])
        if not case['invariants'] or not set(case['invariants']) <= valid:
            raise ValueError('Invalid invariant coverage')
        coverage.update(set(case['invariants']))
        if not case['user_turns'] or not all(isinstance(t, str) and t.strip() for t in case['user_turns']):
            raise ValueError('Empty replay')
        prefix = case.get('prefix_messages', [])
        for i, message in enumerate(prefix):
            if message.get('role') != ('user' if i % 2 == 0 else 'assistant') or not message.get('content', '').strip():
                raise ValueError('Invalid seeded history')
        if prefix and prefix[-1]['role'] != 'assistant':
            raise ValueError('Seeded history must end before the next user input')
        if case['profile'] not in ('no-tools', 'fixture-tools'):
            raise ValueError('Unknown evidence profile')
        for field in ('pass', 'fail', 'category'):
            if not case[field].strip():
                raise ValueError('Missing scoring anchor')
        if (case['profile'] == 'fixture-tools') != bool(case['fixtures']):
            raise ValueError('Fixture profile mismatch')
        for fixture in case['fixtures']:
            path = (ROOT / fixture).resolve()
            if not path.is_relative_to(ROOT / 'evals/fixtures') or not path.is_file():
                raise ValueError('Invalid fixture path')
    if any(coverage[i] < 3 for i in valid):
        raise ValueError('Each invariant needs at least three cases')
    return cases, coverage

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    cases, coverage = cases_from_spec()
    path = ROOT / 'evals/eval_cases.json'
    content = json.dumps(cases, indent=2) + '\n'
    if args.check:
        if not path.exists() or path.read_text() != content:
            parser.exit(1, 'Stale evals/eval_cases.json; run scripts/build_tests.py\n')
    else:
        path.write_text(content)
    print(f'{len(cases)} cases validated; minimum coverage {min(coverage.values())} cases per invariant. No model runs performed.')

if __name__ == '__main__':
    main()
