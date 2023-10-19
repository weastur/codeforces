# URL: https://codeforces.com/problemset/problem/1220/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
s = inp().decode()
one = s.count('n')
zero = s.count('z')
out("1 " * one + "0 " * zero)
