# URL: https://codeforces.com/problemset/problem/1629/A

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
    c = list(zip(a, b))
    c.sort(key=lambda x: x[0])
    for x, y in c:
        if k >= x:
            k += y
        else:
            break
    out(f"{k}\n")
