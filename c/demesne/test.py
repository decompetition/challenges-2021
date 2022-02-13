#! /usr/bin/env python3

import sys
import unittest

import deco

class Tests(unittest.TestCase):
    def assertDomains(self, seed, returncode, expected):
        result = deco.run(seed)
        self.assertEqual(result.returncode, returncode)
        self.assertEqual(result.stderr, '')
        self.assertEqual(result.stdout, '\n'.join(expected) + '\n')

    def test_not_param(self):
        self.assertDomains([], 255, ['Please provide a seed.'])

    def test_first_seed(self):
        expected = [
            "zisbsrns.biz",
            "pofjrycya.biz",
            "emzqrg.biz",
            "csugynhd.biz",
            "rqpnxvwbc.biz",
            "hvbuwk.biz",
            "fbwkwsbg.biz",
            "uzrrv.biz",
            "guywqadyd.biz",
            "wrllp.biz",
            "uxgtoph.biz",
            "jdaawfxkn.biz",
            "zbvivm.biz",
            "whixuub.biz",
            "mfdfubjnq.biz",
            "bkxmtj.biz",
        ]
        self.assertDomains(['0x13371337'], 0, expected);

    def test_second_seed(self):
        expected = [
            "pywolwnvd.biz",
            "ssbzmoy.biz",
            "cvgrf.biz",
            "npukfztj.biz",
            "przvgke.biz",
            "zlenh.biz",
            "knjghuig.biz",
            "uhxqin.biz",
            "anpmnmxo.biz",
            "lpuegx.biz",
            "vjaxhpbji.biz",
            "xlfhhhm.biz",
            "ifsaia.biz",
            "saytjshyf.biz",
            "vcddkls.biz",
            "fwiwk.biz",
        ]
        self.assertDomains(['0x2484A18'], 0, expected);

    def test_third_seed(self):
        expected = [
            "ulomp.biz",
            "entfpncnl.biz",
            "ghyxqfm.biz",
            "rbeir.biz",
            "bdrariic.biz",
            "exwtsbs.biz",
            "oacdt.biz",
            "yupwmlwz.biz",
            "bwupme.biz",
            "lqzzn.biz",
            "wsfsopcn.biz",
            "ymskph.biz",
            "ipxvp.biz",
            "tjdnqkik.biz",
            "vdigrd.biz",
            "gfvrjvefo.biz",
        ]
        self.assertDomains(['0x10'], 0, expected);


if __name__ == '__main__':
    deco.main(sys.argv)
