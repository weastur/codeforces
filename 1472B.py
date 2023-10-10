# URL: https://codeforces.com/problemset/problem/1472/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    if sum(a) % 2 or (n % 2 and not a.count(1)):
        out("NO\n")
    else:
        out("YES\n")
