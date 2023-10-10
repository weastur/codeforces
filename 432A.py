# URL: https://codeforces.com/problemset/problem/432/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n, k = map(int, inp().split())
ans = 0
for y in map(int, inp().split()):
    ans += y + k <= 5
ans //= 3
out(f"{ans}")

