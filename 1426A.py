# URL: https://codeforces.com/problemset/problem/1426/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, x = map(int, inp().split())
    if n <= 2:
        out("1\n")
    else:
        out(f"{((n - 2) + x - 1) // x + 1}\n")
