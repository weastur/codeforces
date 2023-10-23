# URL: https://codeforces.com/problemset/problem/1788/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    c = a.count(2)
    if c == 0:
        out("1\n")
    elif c % 2 != 0:
        out("-1\n")
    else:
        c //= 2
        for i in range(n):
            if a[i] == 2:
                c -= 1
            if c == 0:
                out(f"{i + 1}\n")
                break
