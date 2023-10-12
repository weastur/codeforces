# URL: https://codeforces.com/problemset/problem/1472/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    w, h, n = map(int, inp().split())
    cur = 1
    while w % (cur * 2) == 0:
        cur *= 2
    ww = cur
    cur = 1
    while h % (cur * 2) == 0:
        cur *= 2
    hh = cur
    if ww * hh >= n:
        out("YES\n")
    else:
        out("NO\n")
