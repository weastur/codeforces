# URL: https://codeforces.com/problemset/problem/1829/C

import io
import os
import sys
import math

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = []

a, b, c = [], [], []
for _ in range(int(inp())):
    n = int(inp())
    a.clear()
    b.clear()
    c.clear()
    for _ in range(n):
        m, s = map(int, inp().split())
        if s == 1:
            a.append(m)
        elif s == 10:
            b.append(m)
        elif s == 11:
            c.append(m)
    if not c and not (a and b):
        out.append(-1)
        continue
    ans = 10**9
    if c:
        ans = min(ans, min(c))
    if a and b:
        ans = min(ans, min(a) + min(b))
    out.append(ans)

sys.stdout.write("\n".join(map(str, out)))
