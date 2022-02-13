#! /usr/bin/env python3
import sys
import unittest
import tempfile
import deco

words = ['american', 'test', 'decomperson', 'seclab']

def write_file(f):
    f.write('\n'.join(words))
    f.flush()

class Tests(unittest.TestCase):
    def assert_scaffold(self, params, stdin, output):
        result = deco.run(params, input="\n".join(stdin))
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, output)
        self.assertEqual(result.stderr, '')


    def test_non_existants_wordfile(self):
        result = deco.run(["-w", '/tmp/xyz'])

        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, '')
        self.assertTrue('open /tmp/xyz: no such file or directory' in result.stderr)

    def test_empty_file(self):
        path = '/tmp/emptyfile'
        output = '(________): (s_______): (sc______): (sca_____): (scaff___): (scaffo__): (scaffol_): Yay.\n'
        with open(path, 'w') as f:
            self.assert_scaffold(['-w', path], 'scafold\n', output)

    def test_match(self):
        output = '(____): (t__t): (te_t): You lost your liver!\n(te_t): Yay.\n'
        with tempfile.NamedTemporaryFile('w') as f:
            write_file(f)
            self.assert_scaffold(['-w', f.name, '-s', '10'], 'teas\n', output)

    def test_match2(self):
        output = '(________): (a_____a_): You lost your liver!\n(a_____a_): (a____ca_): You lost your right kidney!\n(a____ca_): You lost your spleen!\n(a____ca_): You lost your pancreas!\n(a____ca_): (am___ca_): (am_r_ca_): (am_rica_): (am_rican): Yay.\n'
        with tempfile.NamedTemporaryFile('w') as f:
            write_file(f)
            self.assert_scaffold(['-w', f.name, '-s', '1'], 'abcdfgmrine\n', output)

    def test_fail(self):
        output = '(___________): You lost your liver!\n(___________): You lost your right kidney!\n(___________): (__c________): (d_c________): (dec___e____): You lost your spleen!\n(dec___e____): You lost your pancreas!\n(dec___e____): You lost your rumen!\n(dec___e____): You lost your esophagus!\n(dec___e____): You lost your head!\nIt was fatal.\n'
        with tempfile.NamedTemporaryFile('w') as f:
            write_file(f)
            self.assert_scaffold(['-w', f.name, '-s', '15'], 'abcdefghilmno\n', output)


if __name__ == '__main__':
    deco.main(sys.argv)
