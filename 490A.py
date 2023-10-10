# URL: https://codeforces.com/problemset/problem/490/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
t1, t2, t3 = [], [], []
for i, x in enumerate(map(int, inp().split())):
    if x == 1:
        t1.append(i + 1)
    elif x == 2:
        t2.append(i + 1)
    else:
        t3.append(i + 1)
w = min(len(t1), len(t2), len(t3))
out(f"{w}\n")
for x, y, z in zip(t1, t2, t3):
    out(f"{x} {y} {z}\n")
