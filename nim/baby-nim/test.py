#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_output(self, args, code, expected):
        result = deco.run(args)

        self.assertEqual(result.returncode, code)
        self.assertEqual(result.stdout,     expected)
        self.assertEqual(result.stderr,     '')


    def test_empty(self):
        self.assert_output([], 1, 'USAGE: ./greet name\n')

    def test_greet(self):
        self.assert_output(['sailor'], 0, 'Hello, sailor!\n')


if __name__ == '__main__':
    deco.main(sys.argv)
