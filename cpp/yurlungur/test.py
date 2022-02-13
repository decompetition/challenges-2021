#! /usr/bin/env python3

import sys
import unittest
import tempfile
import gzip
import base64
# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_yurlungur(self, params, stdin, expected):
        result = deco.run(params, input=stdin)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout,     expected.decode())
        self.assertEqual(result.stderr,     '')


    def test_a(self):
        expected = ''
        self.assert_yurlungur([], '', b'\x1b[0m')

    def test_b(self):
        expected = gzip.decompress(
            base64.b64decode(
                "H4sIAAAAAAAAA5OONrawNrU2NDXNdZSGsk0sc53gbItcZyRxFzjbONcVzjbKdYOxzS1y3WFsC5NcDyRxLulog1wAFmEO1XAAAAA="
            )
        )

        self.assert_yurlungur(['10'], 'ABCDEFGH\n', expected)

    def test_c(self):
        expected = gzip.decompress(
            base64.b64decode(
                "H4sIAAAAAAAAA5OONrawNrU2tDTJNZSGsI2MDXKNYWwjSzjb0NI41xxJPAjONs71RxL3RxIPgem1MIebb2hhhmSmEYINFDdHEueSjjbIBQCRhLdioAAAAA=="
            )
        )

        self.assert_yurlungur(['20'], '1337ROOT1337\n', expected)

    def test_d(self):
        expected = gzip.decompress(
            base64.b64decode(
                "H4sIAAAAAAAAA5OONrawNrU2Nsz1kIYwjUxzHWFMk1xnGNM41xvKNLXM9YQxjXP9YEyTXHco08wAbpilGdwwS1O4YUATvBEmwA0zghtmYQE3DCjqgVDriDABi8uA7uWSjjbIBQDBQAiA1QAAAA=="
            )
        )

        self.assert_yurlungur(['50'], 'HACKINGHACKINGHACK\n', expected)




if __name__ == '__main__':
    deco.main(sys.argv)
