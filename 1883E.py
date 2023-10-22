# URL: https://codeforces.com/contest/1883/problem/E

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
    n = rint()
    a = rlist()
    f = [0] * n
    for i in range(1, n):
        c = 0
        x = a[i - 1]
        y = a[i]
        if a[i] <= a[i - 1]:
            while y < x:
                y *= 2
                c += 1
            f[i] = f[i - 1] + c
        else:
            while x < y:
                x *= 2
                c += 1
            f[i] = max(0, f[i - 1] - c + (x != y))
    ans = sum(f)
    out(f"{ans}\n")
