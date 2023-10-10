# URL: https://codeforces.com/problemset/problem/749/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
k = 0
if n % 2 == 1:
    k = (n - 3) // 2
    out(f"{k + 1}\n3 " + "2 " * k)
else:
    k = n // 2
    out(f"{k}\n" + "2 " * k)
