# URL: https://codeforces.com/problemset/problem/1520/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = inp()
    ans = 9 * (len(n) - 1) + (n[0] - 49) + (int(chr(n[0]) * len(n)) <= int(n))
    out(f"{ans}\n")
