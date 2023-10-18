# URL: https://codeforces.com/problemset/problem/1619/B

import io
import os
import sys
import math

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    x = math.isqrt(n)
    x += (x + 1)**2 <= n
    y = int(math.pow(n, 1.0 / 3))
    y += (y + 1)**3 <= n
    z = int(math.pow(n, 1.0 / 6))
    z += (z + 1)**6 <= n
    ans = x + y - z
    out(f"{ans}\n")
