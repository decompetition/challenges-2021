#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_key(self, key, expected, rc):
        result = deco.run([key])

        self.assertEqual(result.returncode, rc)
        self.assertEqual(result.stdout,     expected + '\n')
        self.assertEqual(result.stderr,     '')

    def test_good(self):
        self.assert_key('26402-OEM-0103863-20000', 'Access Granted!', 0)

    def test_good2(self):
        self.assert_key('23899-OEM-0573643-41700', 'Access Granted!', 0)

    def test_bad(self):
        self.assert_key('23899-XYZ-0573643-41700', 'Invalid Key :(', 255)

    def test_bad2(self):
        self.assert_key('23899-OEM-0573640-41700', 'Invalid Key :(', 255)

    def test_bad3(self):
        self.assert_key('23805-OEM-0573640-41700', 'Invalid Key :(', 255)


if __name__ == '__main__':
    deco.main(sys.argv)
