# URL: https://codeforces.com/problemset/problem/1358/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, m = map(int, inp().split())
    ans = (n // 2) * m + (n % 2) * ((m + 1) // 2)
    out(f"{ans}\n")
