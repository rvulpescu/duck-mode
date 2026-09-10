"""Pipeline checks only: these do not evaluate any model's Duck-mode behavior."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_tests', ROOT / 'scripts/build_tests.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class OwnershipPipeline(unittest.TestCase):
    def test_d16_coverage_and_seed_boundary(self):
        cases, coverage = builder.cases_from_spec()
        self.assertGreaterEqual(coverage['D16'], 6)
        ownership = [c for c in cases if c['id'].startswith('ownership-')]
        self.assertEqual(len(ownership), 6)
        for c in ownership:
            if c.get('prefix_messages'):
                self.assertEqual(c['prefix_messages'][-1]['role'], 'assistant')
                self.assertEqual(len([m for m in c['prefix_messages'] if m['role']=='assistant']), 4)

    def test_adoption_pairs_share_context_but_not_user_development(self):
        cases, _ = builder.cases_from_spec()
        probes = {c['id']: c for c in cases if c['id'].startswith('adoption-')}
        self.assertEqual(len(probes), 6)
        for weak, developed in (
            ('adoption-japan-weak', 'adoption-japan-modified'),
            ('adoption-x3-weak', 'adoption-x3-developed'),
            ('adoption-job-product-weak', 'adoption-job-product-developed'),
        ):
            self.assertEqual(probes[weak]['prefix_messages'], probes[developed]['prefix_messages'])
            self.assertNotEqual(probes[weak]['user_turns'], probes[developed]['user_turns'])
            self.assertIn('D20', probes[weak]['invariants'])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'adoption.json'
            subprocess.run(['python', str(ROOT/'scripts/run_eval.py'), '--case',
                            'adoption-japan-weak', '--model', 'HARNESS-ONLY',
                            '--output', str(path), '--prepare-only'], check=True, capture_output=True)
            packet = json.loads(path.read_text())
            self.assertEqual(packet['status'], 'NOT RUN')
            self.assertTrue(packet['prefix_messages'])
            self.assertFalse({'pass', 'fail', 'category'} & packet.keys())

    def test_graph_invariants_and_reconnect_profiles(self):
        cases, coverage = builder.cases_from_spec()
        for invariant in ('D21', 'D22', 'D23', 'D24'):
            self.assertGreaterEqual(coverage[invariant], 3)
        probes = {c['id']: c for c in cases if c['id'].startswith('graph-')}
        self.assertEqual(len(probes), 8)
        self.assertEqual(probes['graph-evidence-reconnect']['profile'], 'fixture-tools')
        self.assertTrue(probes['graph-evidence-reconnect']['fixtures'])
        with tempfile.TemporaryDirectory() as tmp:
            packet_path = Path(tmp)/'graph.json'
            subprocess.run(['python', str(ROOT/'scripts/run_eval.py'), '--case',
                            'graph-ev-reconnect', '--model', 'HARNESS-ONLY',
                            '--output', str(packet_path), '--prepare-only'], check=True, capture_output=True)
            packet = json.loads(packet_path.read_text())
            self.assertEqual(packet['status'], 'NOT RUN')
            self.assertEqual(packet['user_turns'], probes['graph-ev-reconnect']['user_turns'])
            self.assertFalse({'pass', 'fail', 'category'} & packet.keys())

    def test_landscape_profiles_and_reference_maps(self):
        cases, _ = builder.cases_from_spec()
        probes = [c for c in cases if c['id'].startswith('landscape-')]
        self.assertEqual(len(probes), 4)
        self.assertEqual(sum(c['profile']=='fixture-tools' for c in probes), 1)
        for path in (ROOT/'evals/golden').glob('*.md'):
            content = path.read_text()
            self.assertNotIn('> Distance from', content)
            self.assertNotIn('> Frontier:', content)
            self.assertIn('← 🦆', content)

    def test_frame_escape_profiles_and_inputs(self):
        cases, _ = builder.cases_from_spec()
        probes = {c['id']: c for c in cases if c['id'].startswith('frame-')}
        self.assertEqual(len(probes), 5)
        self.assertTrue(all(len(c['user_turns']) == 4 for c in probes.values()))
        journal = probes['frame-japan-timing']
        self.assertEqual(journal['profile'], 'fixture-tools')
        self.assertTrue(all((ROOT / f).is_file() for f in journal['fixtures']))
        self.assertIn('frame-house-ownership', probes)

    def test_continuation_seed_and_evidence_boundaries(self):
        cases, _ = builder.cases_from_spec()
        probes = {c['id']: c for c in cases if c['id'].startswith('continuation-')}
        self.assertEqual(len(probes), 4)
        self.assertTrue(probes['continuation-starvation-recovery']['prefix_messages'])
        self.assertEqual(len(probes['continuation-evidence-opening']['fixtures']), 2)
        self.assertEqual(probes['continuation-facts-only-boundary']['profile'], 'fixture-tools')

    def test_emergent_map_evidence_profile(self):
        cases, _ = builder.cases_from_spec()
        probes = {c['id']: c for c in cases if c['id'].startswith('emergent-')}
        self.assertEqual(len(probes), 3)
        evidence = probes['emergent-fog-is-not-withholding']
        self.assertEqual(evidence['profile'], 'fixture-tools')
        self.assertTrue(evidence['fixtures'])
        self.assertIn('D04', evidence['invariants'])

    def test_selection_profiles_and_existing_counterexamples(self):
        cases, _ = builder.cases_from_spec()
        selected = {c['id']: c for c in cases}
        probes = [c for c in cases if c['id'].startswith('selection-')]
        self.assertEqual(len(probes), 4)
        self.assertEqual(selected['selection-test-before-introspection']['profile'], 'fixture-tools')
        self.assertTrue(selected['selection-test-before-introspection']['fixtures'])
        self.assertIn('exploration-recognition', selected)
        self.assertIn('d08-1', selected)

    def test_movement_cases_preserve_seeded_and_fresh_modes(self):
        cases, _ = builder.cases_from_spec()
        movement = {c['id']: c for c in cases if c['id'].startswith('movement-')}
        self.assertEqual(len(movement), 4)
        self.assertTrue(movement['movement-jump-after-selection']['prefix_messages'])
        self.assertFalse(movement['movement-reject-and-user-depth'].get('prefix_messages'))
        self.assertIn('D20', movement['movement-jump-after-selection']['invariants'])

    def test_trajectory_invariants_and_counterexamples(self):
        cases, coverage = builder.cases_from_spec()
        for invariant in ('D18', 'D19', 'D20'):
            self.assertGreaterEqual(coverage[invariant], 3)
        selected = {c['id']: c for c in cases}
        self.assertEqual(selected['origin-inventor-selection']['prefix_messages'],
                         selected['origin-user-developed-direction']['prefix_messages'])
        self.assertNotEqual(selected['origin-inventor-selection']['user_turns'],
                            selected['origin-user-developed-direction']['user_turns'])
        self.assertEqual(selected['trajectory-bmw-path']['profile'], 'no-tools')

    def test_navigation_coverage_and_boundary_case(self):
        cases, coverage = builder.cases_from_spec()
        self.assertGreaterEqual(coverage['D17'], 3)
        navigation = [c for c in cases if c['id'].startswith('navigation-')]
        self.assertEqual(len(navigation), 4)
        boundary = next(c for c in navigation if c['id']=='navigation-pressure-boundaries')
        self.assertIn('D10', boundary['invariants'])
        self.assertEqual(boundary['user_turns'][-1], 'Pause.')

    def test_exploration_cases_are_fresh_blind_replays(self):
        cases, _ = builder.cases_from_spec()
        exploration = [c for c in cases if c['id'].startswith('exploration-')]
        self.assertEqual(len(exploration), 7)
        self.assertTrue(all(not c.get('prefix_messages') for c in exploration))
        self.assertTrue(all('D16' in c['invariants'] and 'D13' in c['invariants'] for c in exploration))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'explore.json'
            subprocess.run(['python', str(ROOT/'scripts/run_eval.py'), '--case',
                            'exploration-recognition', '--model', 'HARNESS-ONLY',
                            '--output', str(path), '--prepare-only'], check=True, capture_output=True)
            packet = json.loads(path.read_text())
            self.assertEqual(len(packet['user_turns']), 2)
            self.assertEqual(packet['status'], 'NOT RUN')
            self.assertFalse({'pass', 'fail', 'category'} & packet.keys())

    def test_seed_packet_is_blind_and_not_a_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'packet.json'
            subprocess.run(['python', str(ROOT/'scripts/run_eval.py'), '--case',
                            'ownership-momentum-recovery', '--model', 'HARNESS-ONLY',
                            '--output', str(path), '--prepare-only'], check=True, capture_output=True)
            packet = json.loads(path.read_text())
            self.assertEqual(packet['status'], 'NOT RUN')
            self.assertEqual(packet['transcript'], [])
            self.assertTrue(packet['prefix_messages'])
            self.assertFalse({'pass', 'fail', 'category'} & packet.keys())
            self.assertNotIn('DUCK_TESTS_START', packet['instruction'])

    def test_unloaded_seed_does_not_record_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'run.json'
            subprocess.run(['python', str(ROOT/'scripts/run_eval.py'), '--case',
                            'ownership-one-question-chain', '--model', 'HARNESS-ONLY',
                            '--output', str(path)], input='NO\n', text=True, check=True, capture_output=True)
            self.assertEqual(json.loads(path.read_text())['status'], 'NOT RUN')

    def test_recorded_continuation_excludes_seed_from_model_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'run.json'
            subprocess.run(['python', str(ROOT/'scripts/run_eval.py'), '--case',
                            'ownership-one-question-chain', '--model', 'HARNESS-ONLY',
                            '--output', str(path)], input='READY\nSynthetic harness response.\n.\n',
                           text=True, check=True, capture_output=True)
            packet = json.loads(path.read_text())
            self.assertEqual(packet['status'], 'RECORDED_UNSCORED')
            self.assertEqual(len(packet['transcript']), 1)
            self.assertEqual(packet['checks'], [])

if __name__ == '__main__':
    unittest.main()
