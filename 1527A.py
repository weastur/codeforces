# URL: https://codeforces.com/problemset/problem/1527/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    k = 1 << len(f"{n:b}") - 1
    out(f"{k-1}\n")
