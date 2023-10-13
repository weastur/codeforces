# URL: https://codeforces.com/problemset/problem/1353/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, m = map(int, inp().split())
    ans = 0
    if n == 2:
        ans = m
    elif n > 2:
        ans = 2 * m
    out(f"{ans}\n")
