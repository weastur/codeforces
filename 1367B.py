# URL: https://codeforces.com/problemset/problem/1367/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    x, y = 0, 0
    for i in range(n):
        if i % 2 == 0 and a[i] % 2:
            x += 1
        elif i % 2 and a[i] % 2 == 0:
            y += 1
    if x != y:
        out("-1\n")
    else:
        out(f"{x}\n")
