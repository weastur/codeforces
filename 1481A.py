# URL: https://codeforces.com/problemset/problem/1481/A

import io
import os
import sys
import math

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = []

for _ in range(int(inp())):
    px, py = map(int, inp().split())
    s = inp().decode()
    x, y = False, False
    if (px >= 0 and s.count('R') >= px) or (px < 0 and s.count('L') >= -px):
        x = True
    if (py >= 0 and s.count('U') >= py) or (py < 0 and s.count('D') >= -py):
        y = True
    if x and y:
        out.append("YES")
    else:
        out.append("NO")

sys.stdout.write("\n".join(map(str, out)))
