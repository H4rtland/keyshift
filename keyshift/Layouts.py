'''
Created on 26/08/2016

@author: George
'''

from enum import Enum
from collections import namedtuple

Layout = namedtuple("name", "keys", "large_shift")

"""layouts = {
    "ansi_104":[(0, 12), (0.5, 13), (0.75, 11), (1.25,  10)],
    "ansi_104_bae":[(0, 13), (0.5, 12), (0.75, 11), (1.25,  10)],
    "iso_105":[(0, 12), (0.5, 12), (0.75, 12), (0.25,  11)],
}"""

layouts = {
    "ansi_104":[(0, "1234567890-="), (0.5, "qwertyuiop[]\\"), (0.75, "asdfghjkl;'"), (1.25,  "\\zxcvbnm,./")],
    "ansi_104_bae":[(0, "1234567890-=\\"), (0.5, "qwertyuiop[]"), (0.75, "asdfghjkl;'"), (1.25,  "\\zxcvbnm,./")],
    "iso_105":[(0, "1234567890-="), (0.5, "qwertyuiop[]"), (0.75, "asdfghjkl;'#"), (0.25,  "\\zxcvbnm,./")],
}

#layouts = {
#    "qwerty_small_shift":Layout("QWERTY (SMALL SHIFT)", "1234567890-=QWERTYUIOP[]ASDFGHJKL;'#\\ZXCVBNM,./", False),
#    "qwerty_large_shift":Layout("QWERTY (LARGE SHIFT)", "1234567890-=QWERTYUIOP[]ASDFGHJKL;'#ZXCVBNM,./", True),
#}