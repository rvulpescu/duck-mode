#!/usr/bin/env python3
"""Prepare a blind eval packet, or record a manual external-model replay. No API calls."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', required=True)
    parser.add_argument('--model', required=True, help='Exact model/version as shown by the host')
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--prepare-only', action='store_true', help='Write inputs only; status stays NOT RUN')
    args = parser.parse_args()
    from build_tests import cases_from_spec
    from build_prompts import outputs
    cases, _ = cases_from_spec()
    case = next((c for c in cases if c['id'] == args.case), None)
    if case is None:
        parser.error('Unknown case ID; see evals/eval_cases.json')
    prompt_path = ROOT / 'prompts/generic.md'
    expected = outputs()[prompt_path]
    if not prompt_path.exists() or prompt_path.read_text() != expected:
        parser.error('Runtime prompt is stale; run scripts/build_prompts.py')
    instruction_path = prompt_path
    prompt = instruction_path.read_text()
    # Deliberately exclude pass/fail anchors, categories and reference responses.
    record = dict(case=case['id'], model_version=args.model,
                  date=datetime.now(timezone.utc).isoformat(),
                  prompt_sha256=hashlib.sha256(prompt.encode()).hexdigest(),
                  tool_profile=case['profile'], fixtures=case['fixtures'],
                  instruction_source=str(instruction_path.resolve()),
                  instruction=prompt, prefix_messages=case.get('prefix_messages', []),
                  user_turns=case['user_turns'],
                  status='NOT RUN', transcript=[], checks=[])
    # Exclusive creation prevents accidental destruction of earlier evidence.
    with args.output.open('x') as out:
        json.dump(record, out, indent=2)
        out.write('\n')
    if args.prepare_only:
        print('Blind replay packet saved; no model run performed.')
        return
    print(f'Use a fresh session with {instruction_path} and configure the recorded tool profile.')
    if record['prefix_messages']:
        print('SEEDED continuation test: load prefix_messages from the packet as prior role-labeled context.')
        print('The seeded assistant replies are authored fixtures, not output from the tested model.')
        print('If the host cannot load prior context, leave this packet NOT RUN and use a compatible host.')
        if input('Type READY only after the seed is loaded: ') != 'READY':
            return
    print('Paste each model reply below, ending with a line containing only .')
    print('For fixture-tools, retain tool transcripts separately for scoring. Ctrl-D preserves a partial run.')
    try:
        for turn, user in enumerate(case['user_turns'], 1):
            print(f'\nUser turn {turn}:\n{user}\n\nPaste actual assistant reply:')
            lines = []
            while True:
                line = input()
                if line == '.':
                    if not lines or not '\n'.join(lines).strip():
                        print('An actual nonempty reply is required.')
                        continue
                    break
                lines.append(line)
            record['transcript'].append(dict(turn=turn, user=user, assistant='\n'.join(lines)))
            record['status'] = 'RECORDED_UNSCORED' if turn == len(case['user_turns']) else 'PARTIAL'
            args.output.write_text(json.dumps(record, indent=2) + '\n')
    except (EOFError, KeyboardInterrupt):
        print('\nStopped; previously recorded replies are saved. No compliance score assigned.')
        return
    print('Replay recorded, not scored. Review actual replies and tool evidence against the case and full invariants.')

if __name__ == '__main__':
    main()
