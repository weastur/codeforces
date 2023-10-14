# URL: https://codeforces.com/problemset/problem/1850/C

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    s = []
    for _ in range(8):
        t = inp().decode()
        for x in t:
            if x.isalpha():
                s.append(x)
    out(''.join(s) + '\n')
