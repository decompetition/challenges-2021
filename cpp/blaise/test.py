#! /usr/bin/env python3
import sys
import unittest

import deco

def row(numbers):
    return '\t'.join(str(n) for n in numbers)

class Tests(unittest.TestCase):
    def assert_output(self, args, code, stdout, stderr=''):
        result = deco.run(args)

        self.assertEqual(result.returncode, code)
        self.assertEqual(result.stdout, stdout)
        self.assertEqual(result.stderr, stderr)


    def test_no_args(self):
        self.assert_output([], 1, '', 'USAGE: ./blaise (range)\n')

    def test_bad_arg(self):
        self.assert_output(['76', 'trombones'], 1, '', 'USAGE: ./blaise (range)\n')


    def test_zero(self):
        self.assert_output(['0'], 0, '1\n')

    def test_twelve(self):
        values = [
            [1],
            [1,   1],
            [1,   2,   1],
            [1,   3,   3,   1],
            [1,   4,   6,   4,   1],
            [1,   5,   10,  10,  5,   1],
            [1,   6,   15,  20,  15,  6,   1],
            [1,   7,   21,  35,  35,  21,  7,   1],
            [1,   8,   28,  56,  70,  56,  28,  8,   1],
            [1,   9,   36,  84,  126, 126, 84,  36,  9,   1],
            [1,   10,  45,  120, 210, 252, 210, 120, 45,  10,  1],
            [1,   11,  55,  165, 330, 462, 462, 330, 165, 55,  11,  1],
            [1,   12,  66,  220, 495, 792, 924, 792, 495, 220, 66,  12,  1]
        ]

        output = '\n'.join(row(v) for v in values) + '\n'
        self.assert_output(['12'], 0, output)

    def test_thirteen(self):
        numbers = [1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78,  13,  1]
        output  = '\t'.join(str(n) for n in numbers) + '\n'
        self.assert_output(['13', '13'], 0, output)

    def test_twenties(self):
        values = [
            [1, 21, 210, 1330, 5985,  20349, 54264,  116280, 203490,  293930,  352716,  352716,  293930,  203490,  116280,  54264,   20349,  5985,   1330,   210,   21,    1],
            [1, 22, 231, 1540, 7315,  26334, 74613,  170544, 319770,  497420,  646646,  705432,  646646,  497420,  319770,  170544,  74613,  26334,  7315,   1540,  231,   22,   1],
            [1, 23, 253, 1771, 8855,  33649, 100947, 245157, 490314,  817190,  1144066, 1352078, 1352078, 1144066, 817190,  490314,  245157, 100947, 33649,  8855,  1771,  253,  23,  1],
            [1, 24, 276, 2024, 10626, 42504, 134596, 346104, 735471,  1307504, 1961256, 2496144, 2704156, 2496144, 1961256, 1307504, 735471, 346104, 134596, 42504, 10626, 2024, 276, 24, 1]

        ]

        output = '\n'.join(row(v) for v in values) + '\n'
        self.assert_output(['21', '24'], 0, output)


if __name__ == '__main__':
    deco.main(sys.argv)
