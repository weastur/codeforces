# URL: https://codeforces.com/problemset/problem/1478/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    b = [1] * n
    for i in range(1, n):
        if a[i] == a[i - 1]:
            b[i] = b[i - 1] + 1
    ans = max(b)
    out(f"{ans}\n")
