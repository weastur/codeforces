# URL: https://codeforces.com/problemset/problem/1791/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    c = inp()
    out("YES\n" if b'codeforces'.find(c) != -1 else "NO\n")
