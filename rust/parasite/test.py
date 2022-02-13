#! /usr/bin/env python3

import sys
import unittest
import tempfile

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_output(self, flag, stdin, expect):
        result = deco.run([flag], input=stdin)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, expect)
        self.assertEqual(result.stderr, '')

    def assert_usage(self, args):
        result = deco.run(args, input='hello')

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, 'USAGE: ./parasite -[de]\n')
        self.assertEqual(result.stderr, '')


    def test_no_params(self):
        self.assert_usage([''])

    def test_bad_paramss(self):
        self.assert_usage(['preposterous'])


    def test_encode_empty(self):
        self.assert_output('-e', '', '')

    def test_encode_pair(self):
        self.assert_output('-e', '어', 'KT\n')

    def test_encode_triplet(self):
        self.assert_output('-e', '세', 'GTU\n')
        self.assert_output('-e', '쓰', 'GGD\n')

    def test_encode_quad(self):
        self.assert_output('-e', '였', 'KSGG\n')

    def test_encode_word(self):
        self.assert_output('-e', '맛있다', 'MEG KUGG BE\n')

    def test_encode_words(self):
        self.assert_output('-e', '김치가 맛있다', 'LUM CU LE  MEG KUGG BE\n')

    def test_encode_multine(self):
        self.assert_output('-e',
            '르리에의 그의 집에서 죽은\n'
            '크툴후가 꿈꾸며 기다린다',
            'VD VU KTU KDU  LD KDU  PUW KTU GT  PHL KDF\n'
            'XD ZHV JH LE  LLHM LLH MS  LU BE VUF BE\n'
        )

    def test_encode_invalid(self):
        self.assert_output('-e', 'What is this 김치 stuff anyway?', '   LUM CU\n')


    def test_decode_empty(self):
        self.assert_output('-d', '', '')

    def test_decode_pair(self):
        self.assert_output('-d', 'MA', '모\n')

    def test_decode_triplet(self):
        self.assert_output('-d', 'VIK', '량\n')
        self.assert_output('-d', 'BBA', '또\n')

    def test_decode_quad(self):
        self.assert_output('-d', 'KEFJ', '않\n')

    def test_decode_word(self):
        self.assert_output('-d', 'LLDZ GA VU KDU', '끝소리의\n')

    def test_decode_words(self):
        self.assert_output('-d', 'FEV LEU GTUG  JEF LDV  KUW VSL LU', '날개셋 한글 입력기\n')

    def test_decode_multiline(self):
        self.assert_output('-d',
            'PHL PU  KEFJ KDF  LD LTG KDF  KSK KHTF KDV  PAF PEU JEV  GH  KUGG KD FE\n'
            'LU MN JEF  KSK LTW  GAL KTU GT FDF  PHL KDM ME PT  PHL KDV  PU  MA VDF BE',
            '죽지 않은 그것은 영원을 존재할 수 있으나\n'
            '기묘한 영겁 속에서는 죽음마저 죽을 지 모른다\n'
        )

    def test_decode_invalid(self):
        self.assert_output('-d', 'WHAT IS THIS?', '부 \n')


if __name__ == '__main__':
    deco.main(sys.argv)
