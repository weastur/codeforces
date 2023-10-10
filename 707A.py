# URL: https://codeforces.com/problemset/problem/707/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n, _ = map(int, inp().split())
ans = "#Black&White"
for i in range(n):
    r = inp()
    if r.count(b'Y') + r.count(b'M') + r.count(b'C'):
        ans = "#Color"
        break
out(ans)
