# URL: https://codeforces.com/problemset/problem/1633/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    s = inp().decode()
    x = s.count('0')
    y = len(s) - x
    ans = min(x, y)
    if x == y:
        ans -= 1
    out(f"{ans}\n")
