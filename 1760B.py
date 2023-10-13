# URL: https://codeforces.com/problemset/problem/1760/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    ans = max(inp()) - ord(b'a') + 1
    out(f"{ans}\n")
