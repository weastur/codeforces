# URL: https://codeforces.com/problemset/problem/1791/C

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    s = inp().decode()
    l, r = 0, n - 1
    while l < r:
        if s[l] != s[r]:
            l += 1
            r -= 1
        else:
            break
    ans = r - l + 1
    out(f"{ans}\n")
