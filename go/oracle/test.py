#! /usr/bin/env python3
import sys
import unittest

import deco

class Tests(unittest.TestCase):
    prefix1 = 'I need your DOB, height, weight, name, profession, and eye color seperated by semicolons!\n'
    prefix2 = 'Your prediction:\n'

    def assert_error(self, stdin, message):
        result = deco.run([], input=stdin)

        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, self.prefix1 + message)
        self.assertEqual(result.stderr, '')

    def assert_prediction(self, stdin, message):
        result = deco.run([], input=stdin)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, self.prefix1 + self.prefix2 + message)
        self.assertEqual(result.stderr, '')


    def test_no_input(self):
        self.assert_error('', 'EOF\n')

    def test_not_enough_data(self):
        self.assert_error('aaa;bbb;', 'EOF\n')

    def test_missing_data(self):
        self.assert_error('aaa;bbb;;ccc;', 'String number 3 is empty, try that one again!\nEOF\n')

    def test_success_one(self):
        self.assert_prediction('aaa;bbb;ccc;ddd;eee;fff;', '42\n')

    def test_success_two(self):
        self.assert_prediction('3/17/71;5\'9";130;Bob;jongleur;brown;', 'Look east!\n')


if __name__ == '__main__':
    deco.main(sys.argv)
