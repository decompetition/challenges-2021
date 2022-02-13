#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_output(self, params, expect):
        stdout = 'Γ '
        for val in expect:
            if type(val) is str:
                stdout += val
            else:
                stdout += '= %.6f' % val
            stdout += '\nΓ '

        input  = '\n'.join(str(p) for p in params) + '\n'
        result = deco.run([], input=input)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, stdout)
        self.assertEqual(result.stderr, '')


    def test_no_input(self):
        result = deco.run([], input='')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, 'Γ ')
        self.assertEqual(result.stderr, '')

    def test_invalid(self):
        self.assert_output(['boom'], ['Invalid.'])

    def test_zero(self):
        self.assert_output([0], ['= inf'])

    def test_nan(self):
        self.assert_output([-1234], ['= -nan'])

    def test_positive(self):
        self.assert_output([8], [5040])

    def test_negative(self):
        self.assert_output([-12], [4462937.560822])

    def test_maxima(self):
        self.assert_output([-0.5040830082644554092582693045], [-3.544644])

    def test_positive_loop(self):
        self.assert_output([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0], [
            1,
            0.886227,
            1,
            1.329340,
            2,
            3.323351,
            6,
            11.631728,
            24,
            52.342778,
            120
        ])

    def test_negative_loop(self):
        self.assert_output([-3.0, -2.5, -2.0, -1.5, -1.0, -0.5], [
            -1425169488222640,
            -0.945309,
            +6413262697001885,
            +2.363272,
            -25653050788007544,
            -3.544908
        ])


if __name__ == '__main__':
    deco.main(sys.argv)
