# URL: https://codeforces.com/problemset/problem/1873/C

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

a = [''] * 10
for _ in range(int(inp())):
    for i in range(10):
        a[i] = inp().decode()
    ans = 0
    for i in range(10):
        for j in range(10):
            if a[i][j] != 'X':
                continue
            x = i + 1 if i < 5 else 10 - i
            y = j + 1 if j < 5 else 10 - j
            ans += min(x, y)
    out(f"{ans}\n")
