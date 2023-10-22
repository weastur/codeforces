# URL: https://codeforces.com/contest/1883/problem/G1

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
    a = [1] + rlist()
    b = rlist()
    a.sort()
    b.sort()
    ans = 0
    i, j = 0, 0
    nn = n
    while i < nn:
        if a[i] < b[j]:
            i += 1
            j += 1
        else:
            while j < n and a[i] >= b[j]:
                j += 1
                ans += 1
                nn -= 1
    out(f"{ans}\n")
