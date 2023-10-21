# URL: https://codeforces.com/problemset/problem/1849/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    b, c, h = map(int, inp().split())
    ans = 1 + 2 * min(b - 1, c + h)
    out(f"{ans}\n")
