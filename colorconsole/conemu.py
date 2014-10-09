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
import sys
import msvcrt
from ctypes import windll, byref

from colorconsole.wintypes import CONSOLE_SCREEN_BUFFER_INFO
from colorconsole.ansicodes import escape, codes, colors_bk, colors_fg 

SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo
SetConsoleTitle = windll.kernel32.SetConsoleTitleA
GetConsoleTitle = windll.kernel32.GetConsoleTitleA
SetConsoleCursorPosition = windll.kernel32.SetConsoleCursorPosition
FillConsoleOutputCharacter = windll.kernel32.FillConsoleOutputCharacterA
FillConsoleOutputAttribute = windll.kernel32.FillConsoleOutputAttribute
WaitForSingleObject = windll.kernel32.WaitForSingleObject
ReadConsoleA = windll.kernel32.ReadConsoleA


class Terminal:
    STD_INPUT_HANDLE = -10
    STD_OUTPUT_HANDLE = -11
    WAIT_TIMEOUT = 0x00000102
    WAIT_OBJECT_0 = 0


    def __init__(self):
        self.fg = None
        self.bk = None
        self.havecolor = 1
        self.dotitles = 1
        self.stdout_handle = windll.kernel32.GetStdHandle(Terminal.STD_OUTPUT_HANDLE)
        self.stdin_handle = windll.kernel32.GetStdHandle(Terminal.STD_INPUT_HANDLE)
        self.reset_attrib = self.__get_text_attr()
        self.savedX = 0
        self.savedY = 0
        self.type = "CONEMU"

    def __get_console_info(self):
        csbi = CONSOLE_SCREEN_BUFFER_INFO()
        GetConsoleScreenBufferInfo(self.stdout_handle, byref(csbi))
        return csbi

    def __get_text_attr(self):
        return self.__get_console_info().wAttributes

    def restore_buffered_mode(self):
        pass

    def enable_unbuffered_input_mode(self):
        pass

    def putch(self, ch):
        msvcrt.putc(ch)

    def getch(self):
        return msvcrt.getch()

    def getche(self):
        return msvcrt.getche()

    def kbhit(self, timeout=0):
        return msvcrt.kbhit()

    def no_colors(self):
        self.havecolor = 0

    def set_color(self, fg=None, bk=None):
        if fg is not None:
            sys.stdout.write(escape + colors_fg[fg])
        if bk is not None:
            sys.stdout.write(escape + colors_bk[bk])

    def set_title(self, title):
        if self.type in ["xterm", "Eterm", "aterm", "rxvt", "xterm-color"]:
            sys.stderr.write("\x1b]1;\x07\x1b]2;" + str(title) + "\x07")
            sys.stderr.flush()

    def cprint(self, fg, bk, text):
        self.set_color(fg, bk)
        print (text, end="")

    def print_at(self, x, y, text):
        self.gotoXY(x, y)
        print(text, end="")

    def clear(self):
        sys.stdout.write(codes["clear"])

    def gotoXY(self, x, y):
        sys.stdout.write(codes["gotoxy"].format(y, x))

    def save_pos(self):
        sys.stdout.write(codes["save"])

    def restore_pos(self):
        sys.stdout.write(codes["restore"])

    def reset(self):
        sys.stdout.write(codes["reset"])

    def move_left(self, c=1):
        sys.stdout.write(codes["move_left"].format(c))

    def move_right(self, c=1):
        sys.stdout.write(codes["move_right"].format(c))

    def move_up(self, c=1):
        sys.stdout.write(codes["move_up"].format(c))

    def move_down(self, c=1):
        sys.stdout.write(codes["move_down"].format(c))

    def columns(self):
        csbi = self.__get_console_info()
        return csbi.dwSize.X

    def lines(self):
        csbi = self.__get_console_info()
        return csbi.dwSize.Y

    def underline(self):
        sys.stdout.write(codes["underline"])

    def blink(self):
        sys.stdout.write(codes["blink"])

    def reverse(self):
        sys.stdout.write(codes["reverse"])

    def invisible(self):
        sys.stdout.write(codes["invisible"])

    def reset_colors(self):
        self.default_background()
        self.reset()

    def xterm256_set_fg_color(self, color):
        sys.stdout.write(escape + "38;5;{0}m".format(color))

    def xterm24bit_set_fg_color(self, r, g, b):
        sys.stdout.write(escape + "38;2;{0};{1};{2}m".format(r, g, b))

    def xterm256_set_bk_color(self, color):
        sys.stdout.write(escape + "48;5;{0}m".format(color))

    def xterm24bit_set_bk_color(self, r, g, b):
        sys.stdout.write(escape + "48;2;{0};{1};{2}m".format(r, g, b))

    def default_foreground(self):
        sys.stdout.write(escape + "39m")

    def default_background(self):
        sys.stdout.write(escape + "49m")

