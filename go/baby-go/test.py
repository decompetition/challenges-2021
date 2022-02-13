#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_babygo(self, stdin, expected):
        result = deco.run([], input=stdin)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout,     'Enter string: ' + expected)
        self.assertEqual(result.stderr,     '')

    def test_no_params(self):
        self.assert_babygo('', '')

    def test_lower(self):
        self.assert_babygo('abcdef', 'aBcDeF')

    def test_upper(self):
        self.assert_babygo('BCDEFGHIJK', 'bCdEfGhIjK')

    def test_noise(self):
        self.assert_babygo('#$%&\'(123)*+,-./:;<', '#$%&\'(123)*+,-./:;<')

if __name__ == '__main__':
    deco.main(sys.argv)
