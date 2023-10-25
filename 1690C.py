# URL: https://codeforces.com/problemset/problem/1690/C

import io
import os
import sys
import math

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = []

ans = []
for _ in range(int(inp())):
    n = int(inp())
    s = list(map(int, inp().split()))
    f = list(map(int, inp().split()))
    ans.clear()
    for i in range(n):
        if i == 0 or s[i] >= f[i - 1]:
            ans.append(f[i] - s[i])
        else:
            ans.append(f[i] - f[i - 1])
    out.append(" ".join(map(str, ans)))

sys.stdout.write("\n".join(map(str, out)))
