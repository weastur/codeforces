# URL: https://codeforces.com/problemset/problem/1837/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    x, k = map(int, inp().split())
    if x % k:
        out(f"1\n{x}\n")
    else:
        out(f"2\n{x - 1} 1\n")
