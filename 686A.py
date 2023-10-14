# URL: https://codeforces.com/problemset/problem/686/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n, x = map(int, inp().split())
s = 0
for _ in range(n):
    op, d = inp().split()
    d = int(d)
    if op == b'+':
        x += d
    elif x >= d:
        x -= d
    else:
        s += 1
out(f"{x} {s}")
