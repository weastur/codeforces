# URL: https://codeforces.com/problemset/problem/158/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
a, b, c, d = 0, 0, 0, 0
for x in map(int, inp().split()):
    a += x == 1
    b += x == 2
    c += x == 3
    d += x == 4
ans = d + c
a -= min(a, c)
ans += (b + 1) // 2
a -= min(a, 2 * (b % 2))
ans += (a + 3) // 4
print(ans)
