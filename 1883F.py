# URL: https://codeforces.com/contest/1883/problem/F

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
    l, r = [], []
    x, y = set(), set()
    for i in range(n):
        if a[i] not in x:
            x.add(a[i])
            l.append(i)
    for i in range(n - 1, -1, -1):
        if a[i] not in y:
            y.add(a[i])
            r.append(i)
    r.reverse()
    ans = 0
    rp = 0
    for ll in l:
        while rp < len(r) and r[rp] < ll:
            rp += 1
        ans += len(r) - rp
    out(f"{ans}\n")
