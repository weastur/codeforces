# URL: https://codeforces.com/problemset/problem/1512/B

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
    a, b = None, None
    for i in range(n):
        s = inp().decode()
        for j in range(n):
            if s[j] == '.':
                continue
            if a is None:
                a = (i, j)
            else:
                b = (i, j)
    if a > b:
        a, b = b, a
    if a[0] == b[0]:
        dx = -1 if a[0] > 0 else 1
        c = (a[0] + dx, a[1])
        d = (b[0] + dx, b[1])
    elif a[1] == b[1]:
        dy = -1 if a[1] > 0 else 1
        c = (a[0], a[1] + dy)
        d = (b[0], b[1] + dy)
    else:
        c = (a[0], b[1])
        d = (b[0], a[1])
    ans = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i, j) not in (a, b, c, d):
                row.append('.')
            else:
                row.append('*')
        ans.append(''.join(row))
    out("\n".join(ans) + "\n")
