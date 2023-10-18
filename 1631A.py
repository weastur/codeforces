# URL: https://codeforces.com/problemset/problem/1631/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    a = list(map(int, inp().split()))
    b = list(map(int, inp().split()))
    x = max(min(*c) for c in zip(a, b))
    y = max(*a, *b)
    ans = x * y
    out(f"{ans}\n")
