# URL: https://codeforces.com/problemset/problem/1348/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = 2**n
    for i in range(1, n // 2):
        a += 2**i
    b = 2 * (2**n - 1) - a
    out(f"{abs(a - b)}\n")
