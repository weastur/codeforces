# URL: https://codeforces.com/problemset/problem/1593/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a, b, c = map(int, inp().split())
    mmax = max(a, b, c)
    aa, bb, cc = mmax - a, mmax - b, mmax - c
    if a != mmax or (b == mmax or c == mmax):
        aa += 1
    if b != mmax or (a == mmax or c == mmax):
        bb += 1
    if c != mmax or (a == mmax or b == mmax):
        cc += 1
    out(f"{aa} {bb} {cc}\n")
