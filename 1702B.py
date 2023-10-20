# URL: https://codeforces.com/problemset/problem/1702/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    ans = 1
    d = {}
    for x in inp().decode():
        if len(d) == 3 and x not in d:
            d.clear()
            ans += 1
        d[x] = True
    out(f"{ans}\n")
