# URL: https://codeforces.com/problemset/problem/1660/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a, b = map(int, inp().split())
    if a == 0:
        ans = 1
    else:
        ans = a + b * 2 + 1
    out(f"{ans}\n")
