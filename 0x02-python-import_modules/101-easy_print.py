#!/usr/bin/python3
from ctypes import CDLL;CDLL('libc.so.6').printf("#pythoniscool\n".encode())
