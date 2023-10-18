# URL: https://codeforces.com/problemset/problem/1551/B1

import io
import os
import sys
from collections import Counter

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    c = Counter(inp().decode())
    ans = 0
    x = 0
    for _, cnt in c.most_common():
        ans += (cnt >= 2)
        x += (cnt == 1)
    ans += x // 2
    out(f"{ans}\n")
