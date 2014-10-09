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

escape = "\x1b["

codes = {
    "reset":      escape + "0m",
    "bold":       escape + "01m",
    "clear":      escape + "2J",
    "clear_eol":  escape + "K",
    "gotoxy":     escape + "{0:d};{1:d}H",
    "move_up":    escape + "{0:d}A",
    "move_down":  escape + "{0:d}B",
    "move_right": escape + "{0:d}C",
    "move_left":  escape + "{0:d}D",
    "save":       escape + "s",
    "restore":    escape + "u",
    "dim":        escape + "2m",
    "underline":  escape + "4m",
    "blink":      escape + "5m",
    "reverse":    escape + "7m",
    "invisible":  escape + "8m",
}

colors_fg = {
    0: "30m",
    1: "31m",
    2: "32m",
    3: "33m",
    4: "34m",
    5: "35m",
    6: "36m",
    7: "37m",
    8: "1;30m",
    9: "1;31m",
    10: "1;32m",
    11: "1;33m",
    12: "1;34m",
    13: "1;35m",
    14: "1;36m",
    15: "1;37m",
}

colors_bk = {
    0: "40m",
    1: "41m",
    2: "42m",
    3: "43m",
    4: "44m",
    5: "45m",
    6: "46m",
    7: "47m",
}
