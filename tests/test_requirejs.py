import requirejs
import unittest
import os
import json
import filecmp
import subprocess
import timeit


FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "input")
RJS_PATH = os.path.join(os.path.dirname(__file__), "..", "requirejs", "r.js")


class RequireJSTestCase(unittest.TestCase):
    timings = {}

    def fixture_test(self, fixture):
        path = os.path.join(FIXTURE_PATH, fixture, 'app.build.json')
        with open(path) as f:
            config = json.load(f)

        print()
        dir1 = os.path.join(FIXTURE_PATH, fixture, config['dir'])
        node_time = timeit.timeit(
            lambda: self.compile_node(path),
            number=1,
        )

        config['dir'] += '_2'
        dir2 = os.path.join(FIXTURE_PATH, fixture, config['dir'])
        mr_time = timeit.timeit(
            lambda: self.compile_miniracer(path, config),
            number=1,
        )
        self.timings[fixture] = (node_time, mr_time)

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
        print("Output from 'node r.js -o app.build.json':")
        result = subprocess.call(["node", RJS_PATH, "-o", path])
        self.assertFalse(result, "Node compilation failed")

    @classmethod
    def tearDownClass(cls):
        print()
        print("PyMiniRacer speedup over Node.js subprocess:")
        for name, (node_time, mr_time) in sorted(cls.timings.items()):
            rel_ms = node_time - mr_time
            rel_pct = rel_ms / node_time
            label = name[:8] + (" " * (8 - len(name)))
            print("test_%s: %s%% %s%sms)" % (
                label,
                abs(round(rel_pct * 100, 2)),
                "slower (+" if rel_pct < 0 else "faster (-",
                abs(round(rel_ms * 1000))
            ))


def make_test(name):
    def test_fixture(self):
        self.fixture_test(name)
    return test_fixture


for fixture in os.listdir(FIXTURE_PATH):
    setattr(RequireJSTestCase, 'test_%s' % fixture, make_test(fixture))
