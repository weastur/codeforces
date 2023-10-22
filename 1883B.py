# URL: https://codeforces.com/contest/1883/problem/B

import io
import os
import sys
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


for _ in range(int(inp())):
    n, k = rints()
    c = Counter(inp().decode())
    cnt = 0
    for _, x in c.most_common():
        cnt += x % 2
    if cnt > 0:
        cnt -= 1
    k -= cnt
    if k < 0:
        out("NO\n")
    else:
        out("YES\n")
