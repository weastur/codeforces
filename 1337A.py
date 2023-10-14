# URL: https://codeforces.com/problemset/problem/1337/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a, b, c, _ = map(int, inp().split())
    out(f"{b} {c} {c}\n")
