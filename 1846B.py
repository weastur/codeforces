# URL: https://codeforces.com/problemset/problem/1846/B

import io
import os
import sys
import math

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = []

for _ in range(int(inp())):
    a = inp().decode()
    b = inp().decode()
    c = inp().decode()
    v = (a, b, c, a[0] + b[0] + c[0], a[1] + b[1] + c[1], a[2] + b[2] + c[2],
         a[0] + b[1] + c[2], a[2] + b[1] + c[0])
    if 'XXX' in v:
        out.append('X')
    elif 'OOO' in v:
        out.append('O')
    elif '+++' in v:
        out.append('+')
    else:
        out.append('DRAW')

sys.stdout.write("\n".join(map(str, out)))
