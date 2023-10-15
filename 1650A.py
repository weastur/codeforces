# URL: https://codeforces.com/problemset/problem/1650/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    s = inp().decode()
    c = inp().decode()
    ans = "NO\n"
    for i, x in enumerate(s):
        if x == c and (i + 1) % 2 == 1:
            ans = "YES\n"
    out(ans)
