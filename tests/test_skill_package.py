"""Packaging tests: preserve tested behavior and keep the distributable self-contained."""
import hashlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_skill', ROOT/'scripts/build_skill.py')
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)

class SkillPackageTests(unittest.TestCase):
    def test_contract_bytes_preserved_and_source_not_written(self):
        source = ROOT/'prompts/generic.md'
        before, timestamp = source.read_bytes(), source.stat().st_mtime_ns
        files = package.payloads()
        self.assertEqual(files['SKILL.md'][len(package.FRONTMATTER.encode()):],
                         before[len(package.PREFIX.encode()):])
        self.assertEqual(source.read_bytes(), before)
        self.assertEqual(source.stat().st_mtime_ns, timestamp)

    def test_archive_is_self_contained_and_reproducible(self):
        files = package.payloads()
        archive = package.archive_bytes(files)
        self.assertEqual(archive, package.archive_bytes(files))
        with zipfile.ZipFile(io.BytesIO(archive)) as z:
            self.assertEqual(set(z.namelist()), {'duck-mode/SKILL.md',
                             'duck-mode/agents/openai.yaml', 'duck-mode/LICENSE',
                             'duck-mode/references/examples.md'})
            self.assertIsNone(z.testzip())
            with tempfile.TemporaryDirectory() as tmp:
                z.extractall(tmp)
                for name, data in files.items():
                    self.assertEqual((Path(tmp)/'duck-mode'/name).read_bytes(), data)
        checksum = package.outputs()[ROOT/'dist/duck-mode.zip.sha256'].decode().split()[0]
        self.assertEqual(hashlib.sha256(archive).hexdigest(), checksum)

    def test_invocation_metadata_is_explicit_and_has_launch_prompt(self):
        import yaml
        metadata = yaml.safe_load(package.payloads()['agents/openai.yaml'])
        self.assertIs(metadata['policy']['allow_implicit_invocation'], False)
        self.assertIn('$duck-mode', metadata['interface']['default_prompt'])
        self.assertEqual(metadata['interface']['display_name'], 'Duck-mode')

    def test_unknown_wrapper_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'prompts').mkdir()
            (root/'prompts/generic.md').write_text('Unexpected source')
            with self.assertRaises(ValueError):
                package.payloads(root)

if __name__ == '__main__':
    unittest.main()
