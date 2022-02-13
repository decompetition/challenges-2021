#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_rotterdam(self, params, stdin, expected):
        result = deco.run(params, input=stdin)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout,     expected)
        self.assertEqual(result.stderr,     '')


    def test_no_params(self):
        result = deco.run([])
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout,     '')
        self.assertEqual(result.stderr,     'Key required.\n')

    def test_invalid_key(self):
        result = deco.run(['-k', '50'])
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout,     '')
        self.assertEqual(result.stderr,     'Invalid key: 50\n')

    def test_invalid_file(self):
        filename = '/tmp/ABCD'
        result   = deco.run(['-k', '20', filename])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout,     '')
        self.assertEqual(result.stderr,     'Could not open file: %s\n' % filename)

    def test_one(self):
        self.assert_rotterdam(['-k', '2'], 'ABCD1234EFGH', 'CDEF1234GHIJ')

    def test_two(self):
        self.assert_rotterdam(['-k', '23'], 'fghilmno22pqrs', 'cdefijkl22mnop')


    def test_file(self):
        with tempfile.NamedTemporaryFile('w') as f:
            f.write('0129abcdtuvwxyzABCDEFGHIJK!')
            f.flush()
            self.assert_rotterdam(['-k', '20', '-d', f.name], '', '0129ghijzabcdefGHIJKLMNOPQ!')



if __name__ == '__main__':
    deco.main(sys.argv)
