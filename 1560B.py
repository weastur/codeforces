# URL: https://codeforces.com/problemset/problem/1560/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a, b, c = map(int, inp().split())
    n = abs(a - b) * 2
    if c > n or a > n or b > n:
        ans = -1
    elif c <= n // 2:
        ans = c + n // 2
    else:
        ans = c - n // 2
    out(f"{ans}\n")
