# URL: https://codeforces.com/problemset/problem/1851/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, m, k, h = map(int, inp().split())
    ans = 0
    for x in map(int, inp().split()):
        y = abs(h - x)
        if y % k == 0 and 1 <= y // k <= m - 1:
            ans += 1
    out(f"{ans}\n")
