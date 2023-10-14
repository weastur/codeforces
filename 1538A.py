# URL: https://codeforces.com/problemset/problem/1538/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    x, y = a.index(1), a.index(n)
    if x > y:
        x, y = y, x
    ans = min(x + 1 + n - y, y + 1, n - x)
    out(f"{ans}\n")
