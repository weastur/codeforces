# URL: https://codeforces.com/problemset/problem/1541/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = [i for i in range(1, n + 1)]
    for i in range(1, n, 2):
        a[i], a[i - 1] = a[i - 1], a[i]
    if n % 2:
        a[-1], a[-3] = a[-3], a[-1]
    out(" ".join(map(str, a)) + "\n")
