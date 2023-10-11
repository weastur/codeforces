# URL: https://codeforces.com/problemset/problem/1371/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    if n % 2 == 0:
        ans = n // 2
    else:
        ans = n // 2 + 1
    out(f"{ans}\n")
