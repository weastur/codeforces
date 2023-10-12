# URL: https://codeforces.com/problemset/problem/1742/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    s = set(map(int, inp().split()))
    if len(s) == n:
        out("YES\n")
    else:
        out("NO\n")
