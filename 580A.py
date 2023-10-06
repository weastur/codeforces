# URL: https://codeforces.com/problemset/problem/580/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
a = list(map(int, inp().split()))
d = [0] * n
d[0] = 1
for i in range(1, n):
    if a[i] >= a[i - 1]:
        d[i] = d[i - 1] + 1
    else:
        d[i] = 1
print(max(d))
