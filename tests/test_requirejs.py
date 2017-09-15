import requirejs
import unittest
import os
import json
import filecmp
import subprocess


FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "input")
RJS_PATH = os.path.join(os.path.dirname(__file__), "..", "requirejs", "r.js")


class RequireJSTestCase(unittest.TestCase):
    def fixture_test(self, name):
        path = os.path.join(FIXTURE_PATH, fixture, 'app.build.json')
        with open(path) as f:
            config = json.load(f)

        print()
        dir1 = os.path.join(FIXTURE_PATH, fixture, config['dir'])
        self.compile_node(path)

        config['dir'] += '_2'
        dir2 = os.path.join(FIXTURE_PATH, fixture, config['dir'])
        self.compile_miniracer(path, config)

        def find_diffs(dirs, base=""):
            prefix = base
            if prefix:
                prefix += "/"

            def paths(filenames):
                return " ".join([
                    prefix + filename for filename in filenames
                ])

            self.assertFalse(
                len(dirs.left_only),
                "Only produced by node: " + paths(dirs.left_only)
            )
            self.assertFalse(
                len(dirs.right_only),
                "Not produced by node: " + paths(dirs.right_only)
            )
            self.assertFalse(
                len(dirs.diff_files),
                "Different output: " + paths(dirs.diff_files)
            )
            for path, subdirs in dirs.subdirs.items():
                find_diffs(subdirs, base=prefix + path)

        find_diffs(filecmp.dircmp(
            dir1, dir2,
            ignore=["app.build.json", "build.txt"],
        ))

    def compile_miniracer(self, path, config):
        print("Output from requirejs.optimize():")
        dirname = os.path.dirname(path)
        result = requirejs.optimize(config, working_directory=dirname)
        print(result)

    def compile_node(self, path):
        print("Output from node r.js:")
        result = subprocess.call(["node", RJS_PATH, "-o", path])
        self.assertFalse(result, "Node compilation failed")


for fixture in os.listdir(FIXTURE_PATH):
    def test_fixture(self):
        self.fixture_test(fixture)
    setattr(RequireJSTestCase, 'test_%s' % fixture, test_fixture)
