# URL: https://codeforces.com/problemset/problem/1807/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    a, b = 0, 0
    for x in map(int, inp().split()):
        if x % 2:
            b += x
        else:
            a += x
    if a > b:
        out("YES\n")
    else:
        out("NO\n")
