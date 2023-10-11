# URL: https://codeforces.com/problemset/problem/1722/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

t = str(sorted("Timur"))
for _ in range(int(inp())):
    n = int(inp())
    s = str(sorted(inp().decode()))
    if s == t:
        out("YES\n")
    else:
        out("NO\n")
