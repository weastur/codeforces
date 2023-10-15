# URL: https://codeforces.com/problemset/problem/1690/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    h = (n - 3) // 3
    x = n % 3 + 3
    c = h
    if x == 3:
        a = h + 1
        b = h + 2
    elif x == 4:
        a = h + 1
        b = h + 3
    else:
        a = h + 2
        b = h + 3
    out(f"{a} {b} {c}\n")
