# URL: https://codeforces.com/problemset/problem/144/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
a = list(map(int, inp().split()))
maxp = a.index(max(a))
minp = a[::-1].index(min(a))
print(maxp + minp - (n - minp - 1 < maxp))
