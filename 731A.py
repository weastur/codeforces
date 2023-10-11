# URL: https://codeforces.com/problemset/problem/731/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

ans = 0
pre = ord('a')
for x in inp():
    ans += min(abs(pre - x), 26 - abs(pre - x))
    pre = x
out(f"{ans}")
