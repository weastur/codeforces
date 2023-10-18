# URL: https://codeforces.com/problemset/problem/1729/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    t = inp().decode()
    s = []
    p = n - 1
    while p >= 0:
        if t[p] == '0':
            s.append(chr(ord('a') + int(t[p - 2:p]) - 1))
            p -= 3
        else:
            s.append(chr(ord('a') + int(t[p]) - 1))
            p -= 1
    out("".join(s[::-1]) + '\n')
