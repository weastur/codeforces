# URL: https://codeforces.com/problemset/problem/1859/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    v = max(a)
    b, c = [], []
    for x in a:
        if x == v:
            c.append(x)
        else:
            b.append(x)
    if not b:
        out("-1\n")
    else:
        out(f"{len(b)} {len(c)}\n")
        out(" ".join(map(str, b)) + "\n")
        out(" ".join(map(str, c)) + "\n")
