# URL: https://codeforces.com/problemset/problem/1829/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

f = [0] * 100
for _ in range(int(inp())):
    n = int(inp())
    s = inp().decode().replace(' ', '')
    f[0] = 0 if s[0] == '1' else 1
    for i in range(1, n):
        if s[i] == '1':
            f[i] = 0
        else:
            f[i] = f[i - 1] + 1
    ans = max(f[:n])
    out(f"{ans}\n")
