# URL: https://codeforces.com/problemset/problem/1353/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, k = map(int, inp().split())
    a = list(map(int, inp().split()))
    b = list(map(int, inp().split()))
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if b[i] > a[i]:
            a[i], b[i] = b[i], a[i]
    out(f"{sum(a)}\n")
