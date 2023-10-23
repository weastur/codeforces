# URL: https://codeforces.com/problemset/problem/1719/A

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
    n, m = rints()
    if (n + m) % 2 == 0:
        ans = "Tonya"
    else:
        ans = "Burenka"
    out(f"{ans}\n")
