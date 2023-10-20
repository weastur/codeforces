# URL: https://codeforces.com/problemset/problem/330/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

r, c = map(int, inp().split())
rr, cc = set(), set()
for i in range(1, r + 1):
    for j, x in enumerate(inp().decode()):
        if x == 'S':
            rr.add(i)
            cc.add(j + 1)
ans = (r - len(rr)) * c + (c - len(cc)) * len(rr)
out(f"{ans}")
