#! /usr/bin/env python3

import sys
import unittest
import base64
import gzip
import deco

FIRST_MAZE = """
H4sIAAAAAAAAA41X0XLDMAh75yv0nvMf+uPXLg5IgtzW3FonvcoChPCudf3vio2N+3Wvtq3yLi58
rkV/0/V9HvvggbBvnE2Iifkg1jt/ongWCgQH/N3AEwcPtQtunlt4PmjM/sS+KOKDcNDqm4xdOSom
KnZGzNgTtZ6GRqlMJcuRCE+M/M73WaP65NrQ0xC0Ce95GprJLWvOwm+NqhJcaUgG4DwFRbX1YN4Z
6CqtWsXEju+Jp8e9JG50nowxqYp5Sk1weYZDuAy14t4E64gVRflA06f2o3CnusNZssYW19007jkO
+6XrH4qpuWRlUuUjGRbiahkmr+tMORcZO+Vv6CbyJakuV6V7iDJThyvcmLToPjV4MsThBg9h/fhL
PHnqotWib/7ZZ8h5FqIkZjfEDmhFJi3t0hJ3pHfq6CHu91b3uSe980Nq21Q19JGpnnsKVvfKpfZ8
rqKx1HlcWSCvm7yedotrqod2u/SmulOtqUohWF4p3isUwSdR06f/6ekhe3OamLpOzKoza0hXi/2z
K2DMp9dpyV7NP7Xayvf4ks1Lu5NZ7HUePI81z96hd9nvcz5VpaRP91GdovB8uhcT07hUQ0vchBXV
zkvu8c2TJ4dvfaT8eqebliAzuSaw1GjuzpbVsCjR5h2KZ7Fy35P9ahZ7zw8+7+rRrOZdPy/5DKUz
2Ntp1nYI+a2fPbhmwyzuPi/+6fNC5waKp9XYHE9iR8Nhp0uv2+jIg9epq53Yoa7/4p/ONftompo6
k80/9bTY93npd6sWZHZ4nzcNeB9Z1VG5GM91MNzU0uTAprBr+L/D53zih/HzWWQz7uUU++JLdHIf
mAI6O3wuQzFnz+ieFz1qnyUyi/++Pjx/AB48xT6SEAAA"""

SECOND_MAZE = """
H4sIAAAAAAAAA62aQXbbMBBD93OK2fvphjp8+xqTBD6G7abxiyJLsgkCGAwt5/N8/tej3s6ft98/
25btu8/ldd9r6tP7fXv/9vfo2v48/329Hu19/Hu0dDz91e0bSPQ1+1kdRN9xWlGuY/2zd3Drdr2m
OBJxCh8DwrX3Lr5aGHiEGR35iT3ntpeOjsGVvSFZ1x7UC1fn7Ps8+mi9VFPl17ZesCLzl3HpqonD
L65no3lkX93zfFI5vrLMucYQUZ39SfX3+Os4iFyExsHVum6ox6y8F2eVT5lP7XeeNNJqcN4ayCQn
XoyreN6mky5nK/Ihc4NOoq/Wo16M4Oxkcs2Kb77CL53aOUavxPW36G7y59i8Ks65nROqoiFsOdfO
jteH5OqL0f7uLLIbuNrGVBSszMzdhdtylXXpzsoOdNB+dUy9Ju8oSs+K8yt9KLXyo1P+Wj2UzDv0
adU3+yXnYnnPrM/aI6u6F7na1oOmOm08LL9mJckZ+0HWCXBpfg0ul36UXpP8YpX1iGnuV334okKe
G3nW/NfnXPDFruzeenGFoa+PspR5OaFhZ1x/0YcmnjLhqKPnap+5e8JnbdrRViaLCrqjJ42vjiup
vP58z8Ftg3qC75yP9aqrRkf5lfBmwc/L30RmHutJR1l/Obo32BFeDLmcKxnRa/FWB+xbh9N6gUcR
Too19mQm9aFCTIlbP6LO4i+OxRyYKha/up4gB0PSR/dWvEU9qB01Y880Hdnl+tSAuY11Kc8a/sq6
J0vUMapi5b04a1dBt46fdelsYV14z/u5ZyOHyzJIxraePW95rPTd5xxLfzmX+1nJ2PNodJxe1dbj
K9GQpcYZ9nPLe189wG1D5aXmP39Lx3Emskve0W5c35yXsTU/tTt7yrErwV+q1z3tp2t2riIrO3Wj
2xyb5eqNC/LGTNOMifs5ic/8BKWjP04MkL/MieR2re9NJ+KgA5kj63ypTkyy2/orj3x19LFn/+dZ
d+OjfLEbmz5RhZ5le1aFUZmb7IvCEFbVsf4aunFgmTtm43Mt1OwmUw/WOO7Fcl2m8Xj+lm56v3Bw
cmRCN9ZmLfjrxUjMTGcvf8xfzHBiy9UO19miIxlxV025dnFejWMcH3mSTVV6nuE+U3bwxhHWo7yW
6y/LUr//PFeBfFYpn3+iypy94q7z/tc7cOjc473YreOcYeyOZIlnzV/ppnB4pJZWzF/7I1emnhzM
2u/6i0lERz2BdVK36JnU59YBPDne5fuTQXuUToTurTxaZCmdzX499e6jIzOJnyfhNK/eUyNy34RV
x3455xnWE67IrQch34cKrhuOe8ee+4L2x+FTD2uSuaC1Kbk6zH7IjzlnW3H5+C3rLiTEhblYF3ql
TT5nQoSiNby/eyqfPSNe+1w7eTud7k4zpfP+fTKXdfgIroO53DeelfQb8wSc1Yc8pX+8EjzJ9Lit
Cz31XddUM7K2YlTPeWXF0zTVr+RgXgve6tX6kPc45kS4qnndwVscPbWcrmCSbL6m2V8qsv0K9129
48iuJ/maqrTV95pYrDR2a+9Q0h/Zp+dEoLeGvK3gacr1xidJdsdHc8Jn7lyRrwnjzol77buffC3B
jmrfp00dZ64K8rj5mqqefst0cBb79O2h5geEymxmHnxPp6WG1M5VH77n05zw46phHrf7X6svM8cy
vdizd074WBxZt0SGOcX/wQxJ4N2GLgy+jiZeiVO2Tcz10lF5ImePPVLHf+Rqssa9i6qFWT82Lt2v
WdFYDeH+vXPiKeCo9JnpOOnS5PBSmzqL63qVeHKVwTyx9erpNInhAVa5Yr8i/q8jkbE+b1k76Mik
mFY0C2H0x1SESUuU1H7z5dWm6LILshq8guN70UxQzzReLc/O5zRyNXQb4xH10fG5g5xM6wZFNObE
AyxzqjpS4hzvTwy9D9Xhs/nOgd8riLO7O9VjreorkauN/cw2ogrf/4/Hb1y/AMqRS/TcKQAA"""

THIRD_MAZE = """
H4sIAAAAAAAAA7WaQXbjMAxD9zoF93m6oQ8/0zqy8EEo7abJS8axJZcgSEBK5jVff/8cV13Fh3/+
OrNHXXjPs/fV97nxqv/P+bzW0ffVdyT1fs6vs/drjbpHyvza8+Xa2H9b4+QZP77qhNiPNpZiHAvT
RiFXao+eOrM480F+P24sK8OOYp87MdDxJKzfvDCjwo1mX58FpqoEVymi59w45Tdl+QI6xr4RNCQL
yzR27mjXeefLuVkVqSytGfcx+sV74TMDP9fhwy77JcdchtV66NWyIBUnWDoTGpGfzV21qzC8D1TR
FCyafeYaChFqcgrqe8xwFrpmMS5lxTGkXFxVUmPMLqJxlXJWdk0W7rCRD489HW+M3is+t9dnLSxW
3Y8Ws8pc1VQJpuVj4xBNLomnQjSJtR570rB3Bgai03pRNFOiJhJTB1U4GQdNRl0YS1dDqnWmr6Ad
wyoLMbBjkG1XbN4BfadYmNPOUHf+3lVXu0+RlwkkrK8qxmi9LedaNt6fh0bd1yZZu7p2J7WQuwzF
YSuAXv/CQfAT/Zf9NTR/7iS9r5OnVBvl/C1NLolx1fyjA15zXQumXVPFrlvHcl3lqL1Psqd4Xh6v
1LqZL2Y8dLM6++IU2MUrS3yf9aPRc1XWnTRzdHUs7ilT1oWpwrw31OWZAamx5gdHJtxdko86nkv9
RTthsuqAk1os9WQ1qVUovHSXSEy4euuZrhfi+zGGndti9KyznX2vz/lTvyR2PM5edflOCwvWxLb/
0K62tZd2uHEk62bBUi2erG4866qV8D6aPFtOTwo9sa/0seTooMlkI/niqU84pmNaNVZPzqnBrdvt
6uYxztv3HJ+qx/slYah4ZOu5vYaZjKBFVcWrXAdgPcCdnK/5zz3sONen7kRefU/vT0bY+ke75lGG
cpwP2lKWpmJhzOdcJ1/nrMTM3lf2nZd5RXcYG29KqLkJe2TJJ9QqcePjs34HTXYv6cpgEVf/rMpW
r+JerNX5IdLfs/NGNBDnUz9BZ3vWOY/9w84aHkvqEq+dU/0pksP+RaPzuCIzpn1dyfY6rfXLJw/X
SHnWubHZQ1YfhehTlTkSwyOrGGpf24vx4f3ubCQ81PJnze/ORs11Z6S3sBbpmvueYS+WOOhanJnw
48f3e1Rwl8bXc57KCzVTRs33vXY+9cCp9z/4Pispe3tfn6xeCJxptyiWtAshHyHCiJLY38fjpVxY
dVWPb/uk9xZVkIoxPNfnmvOuz7j746JX7izDKTpTQa1dB0XhX/abBbP8G+fgqJPvyJqfXVOs/eCH
otkyQ1kBL2c9Str7yVePXTSO3e3u0p1eOwpdt7Fpv3g/MMakULL/PSDGrEEE0unuk8k/goaVnFmP
/B1sqpXOga/WPCuGBb1t/tB3vT6ij1TluM+NHc9lkSaMx2iFobDn4XcXdxZZ62CD36M1vaYr7avt
e/7ES6+5T1XYfVZ+S2K1NKWlPuCdFUp3uY/QLwmVu3+L07hK/SNemTue3TBb/KcVKPeao+9Ret57
9ok4HWPNMORvN3ex75XcPegrXDFsV3140frgHt/Xic7V1ZB2x7xsPYZn73xG63qh1flk4Z2P0aul
94T3e9a2jk79JXQF+8Vjp+cU9i82/n6k/3fByIjG8XTHSezE3yuRf1sNuy9irfCM9/XC8CphjJe9
0rtrddCK8Btf2ycSl/ohEBqrqmyj5z/Hmh99RDyC7/va0ioOKwCsAZTBxOm4ivWU+tzdnXg5u6tH
6W8WjBZOzxhLxyZn7NkIv1n0aNcn93Of42jhLxJ1VW1s7AF3w1SROl+O8vdj3E8mJs4KrCMeRlfv
S51LdK1jgKTwnYepAe6KPfLJIXvnJyysLdcx2efGukdPr8zT3SXy0rsAS+Km5zutcTIrvA5e/u75
H8s/jB29FD4oAAA=
"""

class Tests(unittest.TestCase):
    def assertMaze(self, params, expected):
        result = deco.run(params, timeout=0.1)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, '')
        self.assertEqual(result.stdout, expected)

    def test_cow(self):
        result = deco.run(['1', '2'], timeout=0.1)

        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, '')
        self.assertEqual(result.stderr, "You'll never fit a cow in there.\n")

    def test_first_maze(self):
        expected = gzip.decompress(base64.b64decode(FIRST_MAZE)).decode()
        self.assertMaze(['20', '50', '12'], expected)

    def test_second_maze(self):
        expected = gzip.decompress(base64.b64decode(SECOND_MAZE)).decode()
        self.assertMaze(['37', '70', '10', '1337'], expected)

    def test_third_maze(self):
        expected = gzip.decompress(base64.b64decode(THIRD_MAZE)).decode()
        self.assertMaze(['50', '50', '25'], expected)


if __name__ == '__main__':
    deco.main(sys.argv)
