# URL: https://codeforces.com/problemset/problem/1385/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    a = list(map(int, inp().split()))
    a.sort(reverse=True)
    if a[0] != a[1]:
        out("NO\n")
    else:
        out(f"YES\n{a[0]} {a[2]} {a[2]}\n")
