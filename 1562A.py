# URL: https://codeforces.com/problemset/problem/1562/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    l, r = map(int, inp().split())
    if l == r:
        out("0\n")
    else:
        a = r
        b = a // 2 + 1
        if b < l:
            b = l
        ans = a % b
        out(f"{ans}\n")
