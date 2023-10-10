# URL: https://codeforces.com/problemset/problem/1551/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    c1, c2 = n // 3, n // 3
    c1 += n % 3 == 1
    c2 += n % 3 == 2
    out(f"{c1} {c2}\n")
