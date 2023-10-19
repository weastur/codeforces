# URL: https://codeforces.com/problemset/problem/1433/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = inp().decode().replace(' ', '')
    l = a.index('1')
    r = a.rindex('1')
    ans = a[l:r + 1].count('0')
    out(f"{ans}\n")
