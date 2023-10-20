# URL: https://codeforces.com/problemset/problem/1234/A

import io
import os
import sys
import math

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    ans = math.ceil(sum(map(int, inp().split())) / n)
    out(f"{ans}\n")
