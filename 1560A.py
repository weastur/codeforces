# URL: https://codeforces.com/problemset/problem/1560/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

a = [0] * 1000
x = 1
for i in range(1000):
    while x % 3 == 0 or x % 10 == 3:
        x += 1
    a[i] = x
    x += 1
for _ in range(int(inp())):
    k = int(inp())
    out(f"{a[k - 1]}\n")
