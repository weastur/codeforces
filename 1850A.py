# URL: https://codeforces.com/problemset/problem/1850/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a, b, c = map(int, inp().split())
    if a + b >= 10 or a + c >= 10 or b + c >= 10:
        out("YES\n")
    else:
        out("NO\n")
