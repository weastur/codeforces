# URL: https://codeforces.com/contest/1884/problem/C

import io
import os
import sys
import heapq

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
    a = []
    b = []
    for _ in range(n):
        x = tuple(rints())
        if x[0] != 1:
            a.append((x[0], 0))
            a.append((x[1], 1))
        if x[1] != m:
            b.append((x[0], 0))
            b.append((x[1], 1))
    a.sort()
    b.sort()
    ans = 0
    c = 0
    for i in range(len(a)):
        if a[i][1] == 0:
            c += 1
        else:
            c -= 1
        ans = max(ans, c)
    c = 0
    for i in range(len(b)):
        if b[i][1] == 0:
            c += 1
        else:
            c -= 1
        ans = max(ans, c)
    out(f"{ans}\n")
