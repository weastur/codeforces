# URL: https://codeforces.com/problemset/problem/1454/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = [i for i in range(n, 0, -1)]
    if n % 2:
        m = n // 2
        a[0], a[m] = a[m], a[0]
    out(" ".join(map(str, a)) + "\n")
