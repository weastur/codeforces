# URL: https://codeforces.com/problemset/problem/148/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

k, l, m, n = int(inp()), int(inp()), int(inp()), int(inp())
ans = 0
for i in range(1, int(inp()) + 1):
    if i % k and i % l and i % m and i % n:
        continue
    ans += 1
print(ans)
