#!/usr/bin/env python
#
#    colorconsole
#    Copyright (C) 2010 Nilo Menezes
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Inspired/copied/adapted from:
#
# output.py from Gentoo and
# http://code.activestate.com/recipes/572182-how-to-implement-kbhit-on-linux/ and
# http://www.burgaud.com/bring-colors-to-the-windows-console-with-python/
#

# Added for Python 2.6 compatibility
from __future__ import print_function
import os
import sys

import colorconsole.terminal


def test():
    t = colorconsole.terminal.get_terminal()
    t.enable_unbuffered_input_mode()
    t.clear()
    t.gotoXY(0, 0)
    t.set_title("Testing output")
    print("            Foreground 111111")
    print("Background   0123456789012345")
    for b in range(8):
        t.reset()
        print("            ", end="")
        print(b, end="")
        for f in range(16):
            t.cprint(f, b, f % 10)
        print()
    a = 0
    b = 0
    t.reset()
    try:
        while(True):
            t.print_at(a, 20 + b % 20, ".")
            if t.kbhit(0.01):
                t.print_at(50, 6, ord(t.getch()))
            t.print_at(40, 5, "%d %d" % (a, b))
            b += 1
            a = b / 20.0 % 20
            t.print_at(40, 6, b)
            t.print_at(a, 20 + b % 20, "*")
            sys.stdout.flush()
    except KeyboardInterrupt:
        pass
    t.clear()
    t.reset()
    t.restore_buffered_mode()


if __name__ == "__main__":
    test()

