#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_endeavour(self, params, stdin, expected):
        result = deco.run(params, input=stdin)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout,     expected + '\n')
        self.assertEqual(result.stderr,     '')


    def test_no_params(self):
        self.assert_endeavour([''], '', 'USAGE: ./endeavour -[de]')

    def test_valid_encode(self):
        self.assert_endeavour(['-e'], 'ABCDEF', '.- -... -.-. -.. . ..-.')

    def test_valid_encode2(self):
        self.assert_endeavour(['-e'], 'abc10jk', '.- -... -.-. ??.--- -.-')

    def test_valid_decode(self):
        self.assert_endeavour(['-d'], '.- -... -.-. -.. . ..-.', 'ABCDEF')

    def test_valid_decode2(self):
        self.assert_endeavour(['-d'], '... ..- .--. . .-. ... . -.-. .-. . - -- . ... ... .- --. .', 'SUPERSECRETMESSAGE')

    def test_invalid_decode(self):
        self.assert_endeavour(['-d'], '...--...--...', '?')

if __name__ == '__main__':
    deco.main(sys.argv)
