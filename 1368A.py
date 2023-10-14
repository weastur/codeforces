# URL: https://codeforces.com/problemset/problem/1368/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a, b, n = map(int, inp().split())
    ans = 0
    while a <= n and b <= n:
        if a < b:
            a += b
        else:
            b += a
        ans += 1
    out(f"{ans}\n")
