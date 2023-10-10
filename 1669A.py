# URL: https://codeforces.com/problemset/problem/1669/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    r = int(inp())
    d = 4
    if 1400 <= r <= 1599:
        d = 3
    elif 1600 <= r <= 1899:
        d = 2
    elif r >= 1900:
        d = 1
    out(f"Division {d}\n")
