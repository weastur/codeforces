# URL: https://codeforces.com/problemset/problem/1846/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    ans = n
    for _ in range(n):
        a, b = map(int, inp().split())
        ans -= b >= a
    out(f"{ans}\n")
