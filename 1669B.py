# URL: https://codeforces.com/problemset/problem/1669/B

import io
import os
import sys
from collections import Counter

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

mmax = 2 * (10**5)
c = [0] * (mmax + 1)
for _ in range(int(inp())):
    n = int(inp())
    for i in range(1, n + 1):
        c[i] = 0
    ans = -1
    for x in map(int, inp().split()):
        c[x] += 1
        if c[x] == 3:
            ans = x
            break
    out(f"{ans}\n")
