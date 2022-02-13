#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco

COLORS = {
    '@': (22, 34),
    '+': ( 1, 32),
    '-': ( 1, 31)
}

class Tests(unittest.TestCase):
    def assert_output(self, input):
        result = deco.run([], input=input)

        stdout = ''
        for line in input.splitlines():
            style = COLORS.get(line[0])
            if style is not None:
                stdout += "\x1b[%d;%dm%s\x1b[0m\n" % (*style, line)
            else:
                stdout += line + '\n'

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, stdout)
        self.assertEqual(result.stderr, '')


    def test_no_input(self):
        self.assert_output('')

    def test_normal(self):
        self.assert_output('hello')

    def test_metadata(self):
        self.assert_output('@woot')

    def test_insertion(self):
        self.assert_output('+cheeses')

    def test_deletion(self):
        self.assert_output('-infinity')

    def test_everything(self):
        self.assert_output(
            'normal text\n'
            '@but there are changes\n'
            '+sized\n'
            '+fours\n'
            ' unchanging...'
            '-sign\n'
        )


if __name__ == '__main__':
    deco.main(sys.argv)
