# URL: https://codeforces.com/problemset/problem/1729/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a, b, c = map(int, inp().split())
    aa = a - 1
    bb = abs(b - c) + c - 1
    if aa < bb:
        out("1\n")
    elif bb < aa:
        out("2\n")
    else:
        out("3\n")
