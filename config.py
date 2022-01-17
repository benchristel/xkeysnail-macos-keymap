# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

define_keymap(re.compile(".*"), {
    # undo, copy, cut, paste
    K("Super-z"): K("C-z"),
    K("Super-c"): K("C-c"),
    K("Super-x"): K("C-x"),
    K("Super-v"): K("C-v"),

    # save, close, quit
    K("Super-s"): K("C-s"),
    K("Super-w"): K("M-f4"),
    K("Super-q"): K("C-q"),

    # text navigation
    K("Super-RIGHT"): K("END"),
    K("Super-LEFT"): K("HOME"),
    K("Super-UP"): K("C-HOME"),
    K("Super-DOWN"): K("C-END"),
    K("M-LEFT"): K("C-LEFT"),
    K("M-RIGHT"): K("C-RIGHT"),

    # text selection
    K("Super-Shift-RIGHT"): K("Shift-END"),
    K("Super-Shift-LEFT"): K("Shift-HOME"),
    K("Super-Shift-UP"): K("C-Shift-HOME"),
    K("Super-Shift-DOWN"): K("C-Shift-END"),
    K("M-Shift-LEFT"): K("C-Shift-LEFT"),
    K("M-Shift-RIGHT"): K("C-Shift-RIGHT"),
})