# URL: https://codeforces.com/problemset/problem/1517/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    ans = 0
    for i in range(15, -1, -1):
        x = 2050 * 10**i
        ans += n // x
        n %= x
    if ans == 0 or n:
        ans = -1
    out(f"{ans}\n")
