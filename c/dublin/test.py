#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_dublin(self, stdin, expected):
        result = deco.run([], input='\n'.join(stdin))

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout,     expected)
        self.assertEqual(result.stderr,     '')


    def test_none(self):
        self.assert_dublin(['\n'], '')


    def test_one(self):
        self.assert_dublin(['1'], """Forward:
    1st smallest is 1
Reverse:
    1st largest is 1
""")

    def test_two(self):
        self.assert_dublin(['2', '1'], """Forward:
    1st smallest is 1
    2nd smallest is 2
Reverse:
    1st largest is 2
    2nd largest is 1
""")


    def test_three(self):
        self.assert_dublin(['2', '-3', '5'], """Forward:
    1st smallest is -3
    2nd smallest is 2
    3rd smallest is 5
Reverse:
    1st largest is 5
    2nd largest is 2
    3rd largest is -3
""")

    def test_multi(self):
        self.assert_dublin(['-2', '0', '40', '5', '-20', '36'], """Forward:
    1st smallest is -20
    2nd smallest is -2
    3rd smallest is 0
    4th smallest is 5
    5th smallest is 36
    6th smallest is 40
Reverse:
    1st largest is 40
    2nd largest is 36
    3rd largest is 5
    4th largest is 0
    5th largest is -2
    6th largest is -20
""")

if __name__ == '__main__':
    deco.main(sys.argv)
