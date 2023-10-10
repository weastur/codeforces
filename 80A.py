# URL: https://codeforces.com/problemset/problem/80/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n, m = map(int, inp().split())
p = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
if p[p.index(n) + 1] == m:
    out("YES")
else:
    out("NO")
