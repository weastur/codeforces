# URL: https://codeforces.com/problemset/problem/9/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

y, w = map(int, inp().split())
d = 0
ans = {1: "1/6", 2: "1/3", 3: "1/2", 4: "2/3", 5: "5/6", 6: "1/1"}
for i in range(1, 7):
    d += (i >= y and i >= w) or i > max(y, w)
out(ans[d])
