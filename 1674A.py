# URL: https://codeforces.com/problemset/problem/1674/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write


def rint():
    return int(inp())


def rints():
    return map(int, inp().split())


def rlist():
    return list(rints())


for _ in range(int(inp())):
    x, y = rints()
    if y % x:
        out("0 0\n")
        continue
    b = y // x
    out(f"1 {b}\n")
