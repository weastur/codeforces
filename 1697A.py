# URL: https://codeforces.com/problemset/problem/1697/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, m = map(int, inp().split())
    a = list(map(int, inp().split()))
    ans = 0
    for i in range(n):
        if a[i] <= m:
            m -= a[i]
        else:
            ans = sum(a[i:]) - m
            break
    out(f"{ans}\n")
