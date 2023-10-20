# URL: https://codeforces.com/problemset/problem/1843/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    s, k = 0, 0
    a = list(map(int, inp().split()))
    b = [x for x in a if x != 0]
    for i, x in enumerate(b):
        s += x if x > 0 else -x
        if x < 0 and (i == 0 or b[i - 1] > 0):
            k += 1
    out(f"{s} {k}\n")
