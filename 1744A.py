# URL: https://codeforces.com/problemset/problem/1744/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    s = inp().decode()
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = s[i]
        elif d[a[i]] != s[i]:
            out("NO\n")
            break
    else:
        out("YES\n")
