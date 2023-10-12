# URL: https://codeforces.com/problemset/problem/1311/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a, b = map(int, inp().split())
    ans = 0
    if a < b:
        ans = 1 if (b - a) % 2 == 1 else 2
    elif a > b:
        ans = 1 if (a - b) % 2 == 0 else 2
    out(f"{ans}\n")
