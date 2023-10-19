# URL: https://codeforces.com/problemset/problem/1626/A

import io
import os
import sys
from collections import Counter

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    c = Counter(inp().decode())
    s = ''.join(x[0] * x[1] for x in c.most_common())
    out(s + "\n")
