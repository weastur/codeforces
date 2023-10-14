# URL: https://codeforces.com/problemset/problem/1097/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

c = inp()
a = inp().split()
r, m = (x[0] for x in a), (x[1] for x in a)
if c[0] in r or c[1] in m:
    out("YES")
else:
    out("NO")
