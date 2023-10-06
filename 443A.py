# URL: https://codeforces.com/problemset/problem/443/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

s = inp()
if s == b'{}':
    print(0)
else:
    print(len(set(s[1:-1].split(b', '))))
