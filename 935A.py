# URL: https://codeforces.com/problemset/problem/935/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
ans = 0
for i in range(1, n // 2 + 1):
    ans += n % i == 0
out(f"{ans}")
