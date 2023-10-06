# URL: https://codeforces.com/problemset/problem/479/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

a, b, c = int(inp()), int(inp()), int(inp())
print(max(a + b + c, a * b * c, (a + b) * c, a * (b + c)))
