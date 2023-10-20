# URL: https://codeforces.com/problemset/problem/1462/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    s = inp().decode()
    if '2020' in (s[:4], s[-4:], s[0] + s[-3:], s[:2] + s[-2:], s[:3] + s[-1]):
        out("YES\n")
    else:
        out("NO\n")
