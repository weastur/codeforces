# URL: https://codeforces.com/problemset/problem/734/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

a, b, c, d = map(int, inp().split())
x = min(a, c, d)
y = min(a - x, b)
ans = x * 256 + y * 32
out(f"{ans}\n")
