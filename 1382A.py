# URL: https://codeforces.com/problemset/problem/1382/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    a = set(map(int, inp().split()))
    b = set(map(int, inp().split()))
    c = a & b
    if c:
        out(f"YES\n1 {c.pop()}\n")
    else:
        out("NO\n")
