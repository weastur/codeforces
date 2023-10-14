# URL: https://codeforces.com/problemset/problem/1389/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    l, r = map(int, inp().split())
    if 2 * l > r:
        out("-1 -1\n")
    else:
        out(f"{l} {2*l}\n")
