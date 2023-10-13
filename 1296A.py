# URL: https://codeforces.com/problemset/problem/1296/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    cnt = len(list(filter(lambda x: x % 2, a)))
    if (cnt == n and cnt % 2) or (cnt and cnt < n):
        out("YES\n")
    else:
        out("NO\n")
