# URL: https://codeforces.com/problemset/problem/1196/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a = list(map(int, inp().split()))
    a.sort()
    d = a[1] - a[0]
    a[0] += min(d, a[2])
    a[2] -= d
    d = a[2] // 2
    a[0] += d
    a[1] += d
    out(f"{a[0]}\n")
