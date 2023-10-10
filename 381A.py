# URL: https://codeforces.com/problemset/problem/381/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
a = list(map(int, inp().split()))
l, r = 0, n - 1
ans = [0, 0]
g = 0
while r >= l:
    if a[l] >= a[r]:
        ans[g] += a[l]
        l += 1
    else:
        ans[g] += a[r]
        r -= 1
    g = 1 - g
out(f"{ans[0]} {ans[1]}")

