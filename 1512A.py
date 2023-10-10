# URL: https://codeforces.com/problemset/problem/1512/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    a = list(map(int, inp().split()))
    x = a[0] if a[1] != a[2] else a[1]
    for i in range(1, len(a) + 1):
        if a[i - 1] != x:
            out(f"{i}\n")
            break

