# URL: https://codeforces.com/problemset/problem/1400/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    s = inp().decode()
    w = []
    for i in range(1, n + 1):
        w.append(s[2 * i - 2])
    out("".join(w) + "\n")
