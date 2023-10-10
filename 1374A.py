# URL: https://codeforces.com/problemset/problem/1374/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    x, y, n = map(int, inp().split())
    ans = (n // x - (n % x < y)) * x + y
    out(f"{ans}\n")
