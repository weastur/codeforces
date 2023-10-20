# URL: https://codeforces.com/problemset/problem/34/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
a = list(map(int, inp().split()))
x, y, m = 1, n, abs(a[0] - a[n - 1])
for i in range(1, n):
    d = abs(a[i] - a[i - 1])
    if d < m:
        x, y = i + 1, i
        m = d
out(f"{x} {y}\n")
