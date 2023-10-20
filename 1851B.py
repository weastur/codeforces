# URL: https://codeforces.com/problemset/problem/1851/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    for x, y in zip(a, sorted(a)):
        if x % 2 != y % 2:
            out("NO\n")
            break
    else:
        out("YES\n")
