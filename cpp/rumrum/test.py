#! /usr/bin/env python3

import sys
import unittest
import tempfile
import gzip
import base64
# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_rumrum(self, params, expected, timeout=0.1):
        result = deco.run(params.split(" "), timeout=0.2)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout,     '[*] Cracked: ' + expected + '\n')
        self.assertEqual(result.stderr,     '')


    def test_a(self):
        self.assert_rumrum('-h 0x5c48fdd7 -c ABCDEFGH -l 4 ', 'AAAA')

    def test_b(self):
        self.assert_rumrum('-h 0x2e9e2f23 -c ABCTESIL', 'TEST')

    def test_c(self):
        self.assert_rumrum('-h 0xa3e7a371 -c pastc -l 5', 'pasta')


if __name__ == '__main__':
    deco.main(sys.argv)
