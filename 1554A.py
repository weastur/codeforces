# URL: https://codeforces.com/problemset/problem/1554/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    ans = 0
    for i in range(n):
        x = 0 if i == 0 else a[i - 1] * a[i]
        y = 0 if i == n - 1 else a[i + 1] * a[i]
        ans = max(ans, x, y)
    out(f"{ans}\n")
