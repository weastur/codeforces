# URL: https://codeforces.com/contest/1884/problem/A

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
    x, k = rints()
    y = x
    while True:
        s = sum(map(int, list(str(y))))
        if s % k == 0:
            out(f"{y}\n")
            break
        y += 1
