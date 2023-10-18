# URL: https://codeforces.com/problemset/problem/1632/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    s = inp().decode()
    ans = "YES\n" if n <= 2 and s not in ('11', '00') else "NO\n"
    out(ans)
