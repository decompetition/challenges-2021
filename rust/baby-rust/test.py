#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_babyrust(self, params, expected):
        result = deco.run(params)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout,     expected + '\n')
        self.assertEqual(result.stderr,     '')

    def test_no_params(self):
        self.assert_babyrust([], 'tahw')

    def test_even(self):
        x = 'abcdefABCDEF1234'
        self.assert_babyrust([x], x[::-1])

    def test_odd(self):
        x = 'uvwxyzABCDEFGHIJK'
        self.assert_babyrust([x], x[::-1])

    def test_third(self):
        x = '#$%&\'()*+,-./:;<'
        self.assert_babyrust([x], x[::-1])

if __name__ == '__main__':
    deco.main(sys.argv)
