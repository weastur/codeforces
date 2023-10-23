# URL: https://codeforces.com/problemset/problem/1003/A

import io
import os
import sys
from collections import Counter

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

inp()
c = Counter(map(int, inp().split()))
ans = c.most_common()[0][1]
out(f"{ans}\n")
