# URL: https://codeforces.com/problemset/problem/1462/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    b = []
    l, r = 0, n - 1
    k = True
    while l <= r:
        if k:
            x = a[l]
            l += 1
        else:
            x = a[r]
            r -= 1
        k = not k
        b.append(x)
    out(" ".join(map(str, b)) + "\n")
