# URL: https://codeforces.com/problemset/problem/1873/D

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, k = map(int, inp().split())
    s = inp().decode()
    ans = 0
    i = 0
    while i < n:
        if s[i] == 'W':
            i += 1
            continue
        ans += 1
        i += k
    out(f"{ans}\n")
