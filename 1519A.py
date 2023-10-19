# URL: https://codeforces.com/problemset/problem/1519/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    r, b, d = map(int, inp().split())
    x, y = min(r, b), max(r, b)
    if x * (d + 1) >= y:
        out("YES\n")
    else:
        out("NO\n")
