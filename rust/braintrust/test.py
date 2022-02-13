#! /usr/bin/env python3
import sys
import unittest

import deco

class Tests(unittest.TestCase):
    def assert_output(self, program, stdin, output):
        result = deco.run([program], input=stdin)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, output)
        self.assertEqual(result.stderr, '')


    def test_no_input(self):
        self.assert_output('', '', '')

    def test_io(self):
        program = ',.,.,.'
        self.assert_output(program, 'eieio', 'eie')

    def test_cat(self):
        program = ',[.,]'
        self.assert_output(program, 'Meow!', 'Meow!')

    def test_hello_world(self):
        program = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
        self.assert_output(program, '', 'Hello World!\n')

    def test_ascii_val(self):
        program = ',>>++++++++++<<[->+>-[>+>>]>[+[-<+>]>+>>]<<<<<<]>>[-]>>>++++++++++<[->-[>+>>]>[+[-<+>]>+>>]<<<<<]>[-]>>[>++++++[-<++++++++>]<.<<+>+>[-]]<[<[->-<]++++++[->++++++++<]>.[-]]<<++++++[-<++++++++>]<.[-]<<[-<+>]<'
        self.assert_output(program, 'A', '65')

    def test_underflow(self):
        program = ',,,,,,,,,,'
        self.assert_output(program, 'hi', '')

    def test_mismatch(self):
        result  = deco.run([', .,]'], input='Meow?')

        self.assertEqual(result.returncode, 101)
        self.assertIn('panicked', result.stderr)
        self.assertEqual(result.stdout, '')


if __name__ == '__main__':
    deco.main(sys.argv)
