#! /usr/bin/env python3
import sys
import unittest

import deco

class Tests(unittest.TestCase):
    def assert_output(self, stdin, stdout):
        result = deco.run([], input=stdin)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, stdout)
        self.assertEqual(result.stderr, '')

    def test_blank(self):
        self.assert_output('', '')

    def test_upcase(self):
        self.assert_output('hello world', 'Hello World')

    def test_downcase(self):
        self.assert_output('HELLO WORLD', 'Hello World')

    def test_not_letter(self):
        self.assert_output('#blessed', '#blessed')

    def test_multiline(self):
        self.assert_output('abc\n123\ndef', 'Abc\n123\nDef')


if __name__ == '__main__':
    deco.main(sys.argv)
