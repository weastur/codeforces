# URL: https://codeforces.com/problemset/problem/1095/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
t = inp().decode()
p = 0
step = 1
s = []
while p < n:
    s.append(t[p])
    p += step
    step += 1
out("".join(s))
