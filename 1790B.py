# URL: https://codeforces.com/problemset/problem/1790/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, s, r = map(int, inp().split())
    a = [s - r] * n
    c = (n - 1) * (s - r)
    for i in range(1, n):
        if c == r:
            break
        d = min(s - r - 1, c - r)
        c -= d
        a[i] -= d
    out(" ".join(map(str, a)) + "\n")
