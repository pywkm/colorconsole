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

from ctypes import Structure, c_short, c_ushort, c_uint

SHORT = c_short
WORD = c_ushort
DWORD = c_uint

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
WAIT_TIMEOUT = 0x00000102
WAIT_OBJECT_0 = 0


class COORD(Structure):
    """struct in wincon.h."""
    _fields_ = [
        ("X", SHORT),
        ("Y", SHORT)]


class SMALL_RECT(Structure):
    """struct in wincon.h."""
    _fields_ = [
        ("Left", SHORT),
        ("Top", SHORT),
        ("Right", SHORT),
        ("Bottom", SHORT)]


class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    """struct in wincon.h."""
    _fields_ = [
        ("dwSize", COORD),
        ("dwCursorPosition", COORD),
        ("wAttributes", WORD),
        ("srWindow", SMALL_RECT),
        ("dwMaximumWindowSize", COORD)]
