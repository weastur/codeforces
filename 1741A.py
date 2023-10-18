# URL: https://codeforces.com/problemset/problem/1741/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a, b = map(lambda s: s.decode(), inp().split())
    if a == b:
        out("=\n")
        continue
    if a[-1] == 'L':
        x = 2
    elif a[-1] == 'M':
        x = 1
    else:
        x = 0
    if b[-1] == 'L':
        y = 2
    elif b[-1] == 'M':
        y = 1
    else:
        y = 0
    if x < y:
        out("<\n")
        continue
    elif x > y:
        out(">\n")
        continue
    xx = a.count('X')
    yy = b.count('X')
    if (x == 0 and xx > yy) or (x == 2 and xx < yy):
        out("<\n")
    else:
        out(">\n")
