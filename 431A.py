# URL: https://codeforces.com/problemset/problem/431/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

a, b, c, d = map(int, inp().split())
s = inp()
ans = a * s.count(b'1') + b * s.count(b'2') + c * s.count(b'3') + d * s.count(
    b'4')
out(f"{ans}\n")
