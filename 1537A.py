# URL: https://codeforces.com/problemset/problem/1537/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    s = sum(map(int, inp().split()))
    if s < n:
        ans = 1
    else:
        ans = s - n
    out(f"{ans}\n")
