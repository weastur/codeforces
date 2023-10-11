# URL: https://codeforces.com/problemset/problem/1399/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    b = list(map(int, inp().split()))
    ta, tb = min(a), min(b)
    ans = 0
    for x, y in zip(a, b):
        ans += max(x - ta, y - tb)
    out(f"{ans}\n")
