#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco
import gzip
import base64

class Tests(unittest.TestCase):
    def assert_goalie(self, params, expected):
        result = deco.run(params.split(" "))

        expected = gzip.decompress(base64.b64decode(expected)).decode()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout,     expected)
        self.assertEqual(result.stderr,     '')


    def test_help(self):
        result = deco.run(['--help'])
        expected = 'Usage of goalie:\n  -f duration\n    \tframe delay (default 314ms)\n  -h uint\n    \theight (default 20)\n  -n uint\n    \tframes\n  -q\tquiet\n  -s int\n    \tseed\n  -w uint\n    \twidth (default 40)\n'

        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, '')
        self.assertEqual(result.stderr,     expected)

    def test_wrong_param(self):
        result = deco.run(['-X'])
        expected = 'flag provided but not defined: -X\nUsage of goalie:\n  -f duration\n    \tframe delay (default 314ms)\n  -h uint\n    \theight (default 20)\n  -n uint\n    \tframes\n  -q\tquiet\n  -s int\n    \tseed\n  -w uint\n    \twidth (default 40)\n'

        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, '')
        self.assertEqual(result.stderr,     expected)

    def test_a(self):
        expected = "H4sIAAAAAAAAA1NQQAVa2DlcCtiBlhYqnwtdAAcgWh1RqkbVgQC2IOVCktUCY4LqkEhqqAMrQU1VWtjTFVgcSU4LT/rTgpqrhWDjUKeFlcMFAMiJPpP4AgAA"
        self.assert_goalie('-q -h 20 -f 0.0001ms -s 100 -n 40', expected)


    def test_b(self):
        expected = """
H4sIAAAAAAAAA+XWSw7DIAwE0D2n8Hruf8CqH8AYbE8IUiuVRVQprzYYk0QgkHwUYR3Fni4cAOVQ
06WOi9cmn7k6cvdeSeo+K1EOWFayxVvf7kQGB+nXMWV1Io4z8Xynxkb9nPWy8cg6047N+w9u3plt
52zytmPzxi5qvdfdiy4dvItTNofgMO44Ni+DDjk9oxOOzRs7Wyfv+cI6Nu9Z5+12mRRzLuE+y7uD
SPBNUR3I9wzUW26Ft+sHFTDoK50z6r82QYxrL+Z/7acppHXKwjqjlluyWu/R+jmd9St9/2U3Feem
S/Ny59zrgvn73o33AP+gEhRYDAAA
"""
        self.assert_goalie('-q -h 80 -f 0.0001ms -s 20 -n 200', expected)

    def test_c(self):
        expected = """
H4sIAAAAAAAAA4WUURIAEQxD/53Cd+5/wLW0NK2W2VmDJ6JKRzcF8xs/6h19DdSEEMrvkUZak1Q5
Ah0noFuWORUEesAC92stECm3qYgxByzsYtDrKV/5U5M7iIqPOtHbczZH5zH3sORo6V8PpiWVRNCO
tIDdQk3+jiuEuOC6j8f5VoU5L4M7JxF5cYDsNeHAXOYPFswKcUVpbCO2jJ7HXLYcvYRDyVk5vVnl
uZ1sLjmcn3Azg3cO34PJcZG0Vw6Oy4wFPTvVh3Pd/ZUH1liaB/04KvPAKqVofNfeXMU2N6Dvmp/e
PqerXUMYBgAA
"""
        self.assert_goalie('-q -h 40 -f 0.00001ms -s 400 -n 20', expected)


if __name__ == '__main__':
    deco.main(sys.argv)
