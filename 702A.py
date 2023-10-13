# URL: https://codeforces.com/problemset/problem/702/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
a = list(map(int, inp().split()))
f = [1] * n
for i in range(1, n):
    if a[i] > a[i - 1]:
        f[i] = f[i - 1] + 1
ans = max(f)
out(f"{ans}\n")
