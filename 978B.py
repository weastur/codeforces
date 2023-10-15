# URL: https://codeforces.com/problemset/problem/978/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

_ = inp()
s = inp().decode()
ans = 0
while True:
    t = s.replace('xxx', 'xx', 1)
    if len(t) < len(s):
        s = t
        ans += 1
    else:
        break
out(f"{ans}\n")
