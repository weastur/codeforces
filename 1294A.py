# URL: https://codeforces.com/problemset/problem/1294/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a, b, c, n = map(int, inp().split())
    d = max(a, b, c) * 3 - a - b - c
    if n - d >= 0 and (n - d) % 3 == 0:
        out("YES\n")
    else:
        out("NO\n")
