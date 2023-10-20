# URL: https://codeforces.com/problemset/problem/255/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
a = list(map(int, inp().split()))
x = sum(a[::3])
y = sum(a[1::3])
z = sum(a[2::3])
if x > y and x > z:
    out("chest\n")
elif y > z and y > z:
    out("biceps\n")
else:
    out("back\n")
