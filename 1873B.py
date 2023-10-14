# URL: https://codeforces.com/problemset/problem/1873/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    a.sort()
    a[0] += 1
    ans = 1
    for x in a:
        ans *= x
    out(f"{ans}\n")
