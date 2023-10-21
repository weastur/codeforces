# URL: https://codeforces.com/problemset/problem/1391/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, m = map(int, inp().split())
    a = [inp().decode() for _ in range(n)]
    ans = a[-1].count('D')
    for i in range(n):
        ans += a[i][-1] == 'R'
    out(f"{ans}\n")
