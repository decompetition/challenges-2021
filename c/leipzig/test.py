#! /usr/bin/env python3

import sys
import unittest
import base64
import gzip
import deco


class Tests(unittest.TestCase):
    def assert_leipzig(self, params, expected):
        result = deco.run(params)
        self.assertEqual(result.returncode, -2)
        self.assertEqual(result.stderr, '')
        self.assertEqual(result.stdout, str(expected))


    def test_none(self):
        result = deco.run([])
        self.assertEqual(result.returncode, -6)
        self.assertEqual(result.stderr, 'Nein!\n')

    def test_zero(self):
        result = deco.run(['0'])
        self.assertEqual(result.returncode, -6)
        self.assertEqual(result.stderr, 'Nein...\n')

    def test_one(self):
        self.assert_leipzig(['50'], 24)

    def test_two(self):
        self.assert_leipzig(['12'], 9)

    def test_three(self):
        self.assert_leipzig(['123'], 46)


if __name__ == '__main__':
    deco.main(sys.argv)
