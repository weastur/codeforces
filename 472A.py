# URL: https://codeforces.com/problemset/problem/472/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
if n % 2 == 0:
    out(f"4 {n - 4}")
else:
    out(f"9 {n - 9}")

