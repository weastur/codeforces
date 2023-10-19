# URL: https://codeforces.com/problemset/problem/1660/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    a.sort(reverse=True)
    if (n == 1 and a[0] == 1) or (n > 1 and a[0] - a[1] <= 1):
        out("YES\n")
    else:
        out("NO\n")
