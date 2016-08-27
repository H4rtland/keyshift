'''
Created on 26/08/2016

@author: George
'''

order = ["iso_105", "ansi_104", "ansi_104_bae", "AZERTY"]

layouts = {
    "ansi_104":[(0, "1234567890-="), (0.5, "QWERTYUIOP[]\\"), (0.75, "ASDFGHJKL;'"), (1.25,  "ZXCVBNM,./")],
    "ansi_104_bae":[(0, "1234567890-=\\"), (0.5, "QWERTYUIOP[]"), (0.75, "ASDFGHJKL;'"), (1.25,  "ZXCVBNM,./")],
    "iso_105":[(0, "1234567890-="), (0.5, "QWERTYUIOP[]"), (0.75, "ASDFGHJKL;'#"), (0.25,  "\\ZXCVBNM,./")],
    "AZERTY":[(0, "1234567890°+"), (0.5, "AZERTYUIOP¨£"), (0.75, "QSDFGHJKLM%µ"), (0.25,  "<WXCVBN?./§")],
}

names = {
    "ansi_104":"ANSI 104",
    "ansi_104_bae":"ANSI 104 BAE",
    "iso_105":"ISO 105",
    "AZERTY":"AZERTY",
}