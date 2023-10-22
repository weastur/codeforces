# URL: https://codeforces.com/contest/1883/problem/A

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
    s = inp().decode()
    ans = 0
    last = 1
    for x in s:
        c = int(x)
        if c == 0:
            c = 10
        ans += abs(last - c) + 1
        last = c
    out(f"{ans}\n")
