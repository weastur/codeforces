# URL: https://codeforces.com/problemset/problem/405/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

_ = inp()
a = list(map(int, inp().split()))
a.sort()
out(" ".join(map(str, a)))
