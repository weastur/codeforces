# URL: https://codeforces.com/problemset/problem/509/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
a = [[0] * n for _ in range(n)]
for i in range(n):
    a[0][i] = 1
ans = 1
for i in range(1, n):
    for j in range(n):
        if j == 0:
            a[i][j] = 1
        else:
            a[i][j] = a[i - 1][j] + a[i][j - 1]
        ans = max(ans, a[i][j])
out(f"{ans}")
