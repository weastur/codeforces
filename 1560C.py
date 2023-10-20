# URL: https://codeforces.com/problemset/problem/1560/C

import io
import os
import sys
import math

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = math.isqrt(n)
    if n == a * a:
        out(f"{a} {1}\n")
    else:
        n -= a * a
        if n <= a + 1:
            c = a + 1
            r = n
        else:
            r = a + 1
            c = a + 1 - (n - a - 1)
        out(f"{r} {c}\n")
