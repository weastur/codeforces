# URL: https://codeforces.com/problemset/problem/1454/B

import io
import os
import sys
from collections import Counter

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    a = list(map(int, inp().split()))
    c = Counter(a)
    b = [x[0] for x in c.most_common() if x[1] == 1]
    if not b:
        ans = -1
    else:
        ans = a.index(min(b)) + 1
    out(f"{ans}\n")
