# URL: https://codeforces.com/problemset/problem/1722/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    a, b = inp(), inp()
    if a.replace(b'B', b'G') == b.replace(b'B', b'G'):
        out("YES\n")
    else:
        out("NO\n")
