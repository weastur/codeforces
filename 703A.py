# URL: https://codeforces.com/problemset/problem/703/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

tm, tc = 0, 0
for _ in range(int(inp())):
    m, c = map(int, inp().split())
    tm += m > c
    tc += m < c
if tm > tc:
    out("Mishka")
elif tm < tc:
    out("Chris")
else:
    out("Friendship is magic!^^")
