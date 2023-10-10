# URL: https://codeforces.com/problemset/problem/1520/A

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
    ans = True
    pre = None
    for x in inp():
        if c[x] and pre != x:
            ans = False
            break
        c[x] += 1
        pre = x
    out("YES\n" if ans else "NO\n")
