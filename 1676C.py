# URL: https://codeforces.com/problemset/problem/1676/C

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, m = map(int, inp().split())
    a = []
    for _ in range(n):
        a.append(inp().decode())
    ans = 100500
    for i in range(n):
        for j in range(i + 1, n):
            cur = 0
            for k in range(m):
                cur += abs(ord(a[i][k]) - ord(a[j][k]))
            ans = min(ans, cur)
    out(f"{ans}\n")
