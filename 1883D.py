# URL: https://codeforces.com/contest/1883/problem/D

import io
import os
import sys
import heapq
from collections import Counter

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write


def rint():
    return int(inp())


def rints():
    return map(int, inp().split())


def rlist():
    return list(rints())


l, r = [], []
lc, rc = Counter(), Counter()
for _ in range(int(inp())):
    raw = inp().split()
    op, a, b = raw[0].decode(), int(raw[1]), int(raw[2])
    if op == '+':
        heapq.heappush(r, b)
        heapq.heappush(l, -a)
    elif op == '-':
        lc[a] += 1
        rc[b] += 1
    x, y = -l[0], r[0]
    while l and lc[x]:
        heapq.heappop(l)
        lc[x] -= 1
        if l:
            x = -l[0]
        else:
            x = None
    while r and rc[y]:
        heapq.heappop(r)
        rc[y] -= 1
        if r:
            y = r[0]
        else:
            y = None
    if x and y and x > y:
        out("YES\n")
    else:
        out("NO\n")
