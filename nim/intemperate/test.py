#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_output(self, value, unit, code, expected):
        result = deco.run([str(value), unit])

        self.assertEqual(result.returncode, code)
        self.assertEqual(result.stdout,     expected)
        self.assertEqual(result.stderr,     '')


    def test_no_params(self):
        result = deco.run([])

        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, 'USAGE: ./convert value unit\n')
        self.assertEqual(result.stderr, '')

    def test_bad_number(self):
        self.assert_output('eleventy', 'K', 32, (
            "Invalid number.\n"
        ))

    def test_bad_unit(self):
        self.assert_output(99, 'Luftballons', 212, (
            "Unknown unit.\n"
        ))


    def test_kelvin(self):
        self.assert_output(500, 'K', 0, (
            "=  500.00 K\n"
            "=  226.85 C\n"
            "=  440.33 F\n"
        ))

    def test_celsius(self):
        self.assert_output(4, 'C', 0, (
            "=  277.15 K\n"
            "=    4.00 C\n"
            "=   39.20 F\n"
        ))

    def test_farenheit(self):
        self.assert_output(-10, 'F', 0, (
            "=  249.82 K\n"
            "=  -23.33 C\n"
            "=  -10.00 F\n"
        ))


if __name__ == '__main__':
    deco.main(sys.argv)
