#! /usr/bin/env python3
import sys
import unittest

import deco

class Tests(unittest.TestCase):
    def assert_output(self, args, code, stdout, stderr):
        result = deco.run(args)

        self.assertEqual(result.returncode, code)
        self.assertEqual(result.stdout, stdout)
        self.assertEqual(result.stderr, stderr)

    def test_no_args(self):
        self.assert_output([], 2, '', 'USAGE: ./grade n\n')

    def test_bad_arg(self):
        self.assert_output(['film'], 2, '', 'Don\'t be so negative.\n')

    def test_negative_arg(self):
        self.assert_output(['-42'], 2, '', 'Don\'t be so negative.\n')

    def test_1(self):
        self.assert_output(['1'], 0, 'Perfect!\n', '')

    def test_72(self):
        self.assert_output(['72'], 1, 'Needs improvement.\n', '')

    def test_496(self):
        self.assert_output(['496'], 0, 'Perfect!\n', '')


if __name__ == '__main__':
    deco.main(sys.argv)
