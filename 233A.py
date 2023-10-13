# URL: https://codeforces.com/problemset/problem/233/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
if n % 2:
    out("-1")
else:
    p = [i + 1 if i % 2 else i - 1 for i in range(1, n + 1)]
    out(" ".join(map(str, p)))
