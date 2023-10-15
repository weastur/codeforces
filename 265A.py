# URL: https://codeforces.com/problemset/problem/265/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

s = inp().decode()
t = inp().decode()
ans = 0
for x in t:
    if x == s[ans]:
        ans += 1
out(f"{ans+1}\n")
