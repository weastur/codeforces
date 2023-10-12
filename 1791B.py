# URL: https://codeforces.com/problemset/problem/1791/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    x, y = 0, 0
    _ = inp()
    ans = False
    for d in inp().decode():
        if d == 'L':
            x -= 1
        elif d == 'R':
            x += 1
        elif d == 'D':
            y -= 1
        else:
            y += 1
        ans |= x == 1 and y == 1
    out("YES\n" if ans else "NO\n")
