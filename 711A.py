# URL: https://codeforces.com/problemset/problem/711/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
a = []
replaced = False
for _ in range(n):
    s = inp().decode()
    if not replaced:
        t = s.replace('OO', '++', 1)
        replaced = s != t
        s = t
    a.append(s)
if replaced:
    out("YES\n")
    out("\n".join(a))
else:
    out("NO")
