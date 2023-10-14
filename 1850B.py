# URL: https://codeforces.com/problemset/problem/1850/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    ans, val = 0, 0
    for i in range(int(inp())):
        a, b = map(int, inp().split())
        if a <= 10 and b > val:
            ans = i + 1
            val = b
    out(f"{ans}\n")
