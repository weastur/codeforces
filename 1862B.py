# URL: https://codeforces.com/problemset/problem/1862/B

import io
import os
import sys
import math

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = []

a = []
for _ in range(int(inp())):
    n = int(inp())
    b = list(map(int, inp().split()))
    a.clear()
    a.append(b[0])
    for i in range(1, n):
        a.append(b[i])
        if b[i] < b[i - 1]:
            a.append(b[i])
    out.append(len(a))
    out.append(" ".join(map(str, a)))

sys.stdout.write("\n".join(map(str, out)))
