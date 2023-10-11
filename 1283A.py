# URL: https://codeforces.com/problemset/problem/1283/A?locale=ru

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    h, m = map(int, inp().split())
    ans = 1440 - (h * 60 + m)
    out(f"{ans}\n")
