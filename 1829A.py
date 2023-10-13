# URL: https://codeforces.com/problemset/problem/1829/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    s = inp().decode()
    ans = len(list(filter(lambda x: x[0] != x[1], zip(s, "codeforces"))))
    out(f"{ans}\n")
