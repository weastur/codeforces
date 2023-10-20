# URL: https://codeforces.com/problemset/problem/1855/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    c = 0
    for i, x in enumerate(map(int, inp().split())):
        c += x == i + 1
    ans = (c + 1) // 2
    out(f"{ans}\n")
