# URL: https://codeforces.com/problemset/problem/1285/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

_ = inp()
s = inp().decode()
ans = s.count('L') + s.count('R') + 1
out(f"{ans}")
