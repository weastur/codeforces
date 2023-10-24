# URL: https://codeforces.com/problemset/problem/1304/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = []

for _ in range(int(inp())):
    x, y, a, b = map(int, inp().split())
    t, k = divmod(y - x, a + b)
    if k:
        out.append(-1)
    else:
        out.append(t)

sys.stdout.write("\n".join(map(str, out)))
