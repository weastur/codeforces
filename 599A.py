# URL: https://codeforces.com/problemset/problem/599/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

d1, d2, d3 = map(int, inp().split())
d = min(d1 + d2, d3)
d1h = min(d1, d2 + d3)
d2h = min(d2, d1 + d3)
ans = min(d1 + d + d2h, d2 + d + d1h)
out(f"{ans}\n")
