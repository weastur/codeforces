# URL: https://codeforces.com/problemset/problem/1388/A

import io
import os
import sys
import math

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = []

for _ in range(int(inp())):
    n = int(inp())
    if n <= 30:
        out.append("NO")
    elif n in (36, 40, 44):
        out.append(f"YES\n{n - 31} 15 10 6")
    else:
        out.append(f"YES\n{n - 30} 14 10 6")

sys.stdout.write("\n".join(map(str, out)))
