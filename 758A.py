# URL: https://codeforces.com/problemset/problem/758/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

_ = inp()
a = list(map(int, inp().split()))
m = max(a)
ans = 0
for x in a:
    ans += m - x
out(f"{ans}")

