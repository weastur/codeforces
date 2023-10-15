# URL: https://codeforces.com/problemset/problem/1473/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, d = map(int, inp().split())
    a = sorted(map(int, inp().split()))
    if a[n - 1] <= d or a[0] + a[1] <= d:
        out("YES\n")
    else:
        out("NO\n")
