# URL: https://codeforces.com/problemset/problem/1397/A

import io
import os
import sys
from collections import Counter

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    c = Counter()
    for _ in range(n):
        c.update(inp().decode())
    for _, cnt in c.most_common():
        if cnt % n:
            out("NO\n")
            break
    else:
        out("YES\n")
