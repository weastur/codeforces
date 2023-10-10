# URL: https://codeforces.com/problemset/problem/492/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
total = 0
for i in range(1, n + 1):
    total += (i * (i + 1)) // 2
    if total + ((i + 1) * (i + 2)) // 2 > n:
        out(f"{i}")
        break
