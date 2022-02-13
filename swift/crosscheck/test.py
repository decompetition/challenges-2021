#! /usr/bin/env python3
import sys
import unittest

import deco

class Tests(unittest.TestCase):
    wordfile = '/tmp/words.txt'

    @classmethod
    def setUpClass(cls):
        with open(cls.wordfile, 'w') as file:
            file.write(
                'aries\n'
                'taurus\n'
                'gemini\n'
                'cancer\n'
                'leo\n'
                'virgo\n'
                'libra\n'
                'scorpio\n'
                'sagittarius\n'
                'capricorn\n'
                'aquarius\n'
                'pisces\n'
            )

    def assert_error(self, args, stdout):
        result = deco.run(args)

        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, stdout)
        self.assertEqual(result.stderr, '')

    def assert_pass(self, input):
        result = deco.run([self.wordfile], input=input)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')
        self.assertEqual(result.stderr, '')

    def assert_fail(self, invalid, input):
        result = deco.run([self.wordfile], input=input)
        stdout = 'Invalid words:\n'
        for word in invalid:
            stdout += ' - ' +  word + '\n'

        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, stdout)
        self.assertEqual(result.stderr, '')


    def test_usage(self):
        self.assert_error(['one', 'two'], 'USAGE: ./crosscheck [words-file]\n')

    def test_bad_file(self):
        self.assert_error(['/i/do/not/exist'], 'Could not open words file.\n')

    def test_no_input(self):
        self.assert_pass('')

    def test_blank_input(self):
        self.assert_pass(
            '   \n'
            '     \n'
            '  \n'
            '       \n'
            '    \n'
        )

    def test_valid_horizontal(self):
        self.assert_pass('capricorn leo')

    def test_valid_vertical(self):
        self.assert_pass('\n'.join('pisces virgo'))

    def test_invalid_horizontal(self):
        self.assert_fail(['draco'], 'draco aquarius')

    def test_invalid_vertical(self):
        self.assert_fail(['cassiopeia'], '\n'.join('cancer cassiopeia'))

    def test_ragged_margin(self):
        self.maxDiff = None
        self.assert_pass('\n'.join('scorpio') + '\n\n' + '\n'.join('libra'))
        self.assert_fail(['cats', 'dogs'], '\n'.join('cats') + '\n\n' + '\n'.join('dogs'))

    def test_big_pass(self):
        self.maxDiff = None
        self.assert_pass(
            '       s \n'
            'libra  c t  \n'
            '       o a\n'
            'sagittarius leo\n'
            ' q     p r\n'
            ' u v   i u  \n'
            ' aries o s    \n'
            ' r r\n'
            ' i gemini   \n'
            ' u o\n'
            ' s          \n'
        )

    def test_big_fail(self):
        self.assert_fail(['librum', 'solar', 'ice'],
            '       s \n'
            'librum c t  \n'
            '       o a\n'
            'sagittarius leo\n'
            ' q     p r\n'
            ' u v   i u  \n'
            ' aries o solar\n'
            ' r r\n'
            ' i gemini   \n'
            ' u o    c\n'
            ' s      e   \n'
        )


if __name__ == '__main__':
    deco.main(sys.argv)
