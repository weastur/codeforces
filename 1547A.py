# URL: https://codeforces.com/problemset/problem/1547/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    x1, y1 = map(int, inp().split())
    x2, y2 = map(int, inp().split())
    x3, y3 = map(int, inp().split())
    ans = abs(x1 - x2) + abs(y1 - y2)
    if (x1 == x2 == x3 and (y1 <= y3 <= y2 or y2 <= y3 <= y1)) or (
            y1 == y2 == y3 and (x1 <= x3 <= x2 or x2 <= x3 <= x1)):
        ans += 2
    out(f"{ans}\n")
