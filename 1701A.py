# URL: https://codeforces.com/problemset/problem/1701/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a, b = map(int, inp().split())
    c, d = map(int, inp().split())
    ans = 1
    if a + b + c + d == 0:
        ans = 0
    elif a + b + c + d == 4:
        ans = 2
    out(f"{ans}\n")
