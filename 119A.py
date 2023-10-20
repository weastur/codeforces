# URL: https://codeforces.com/problemset/problem/119/A

import io
import os
import sys
import math

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

a, b, n = map(int, inp().split())
d = 0
while n:
    if d == 0:
        g = math.gcd(n, a)
    else:
        g = math.gcd(n, b)
    n -= g
    d = 1 - d
out(f"{1 - d}")
