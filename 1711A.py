# URL: https://codeforces.com/problemset/problem/1711/A

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
    a.clear()
    a.append(n)
    for x in range(1, n):
        a.append(x)
    out.append(" ".join(map(str, a)))

sys.stdout.write("\n".join(map(str, out)))
