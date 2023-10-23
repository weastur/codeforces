# URL: https://codeforces.com/problemset/problem/1569/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    s = inp().decode()
    for i in range(1, n):
        if s[i] != s[i - 1]:
            out(f"{i} {i + 1}\n")
            break
    else:
        out("-1 -1\n")
