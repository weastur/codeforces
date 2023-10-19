# URL: https://codeforces.com/problemset/problem/1811/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, d = map(int, inp().split())
    s = inp().decode()
    t = None
    for i in range(n):
        if ord(s[i]) - ord('0') < d:
            t = s[:i] + str(d) + s[i:]
            break
    if t is None:
        t = s + str(d)
    out(t + "\n")
