# URL: https://codeforces.com/problemset/problem/1385/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    s = set()
    a = []
    for x in map(int, inp().split()):
        if x not in s:
            a.append(x)
            s.add(x)
    out(" ".join(map(str, a)) + '\n')
