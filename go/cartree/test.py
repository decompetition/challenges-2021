#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_rotterdam(self, stdin, expected):
        result = deco.run([], input=stdin)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout,     expected + '\n')
        self.assertEqual(result.stderr,     '')


    def test_no_params(self):
        self.assert_rotterdam('', '-')

    def test_a(self):
        self.assert_rotterdam('1\n2\n3\n4\n', '(- 1 (- 2 (- 3 4)))')

    def test_b(self):
        self.assert_rotterdam('4\n3\n2\n1\n', '(((4 3 -) 2 -) 1 -)')

    def test_c(self):
        self.assert_rotterdam('1A4B2C0D10E7A', '((- 1 (4 2 -)) 0 (10 7 -))')

if __name__ == '__main__':
    deco.main(sys.argv)
