# URL: https://codeforces.com/problemset/problem/1714/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    a.reverse()
    d = {}
    ans = 0
    for i, x in enumerate(a):
        if x in d:
            ans = n - i
            break
        else:
            d[x] = True
    out(f"{ans}\n")
