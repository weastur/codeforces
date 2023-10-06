# URL: https://codeforces.com/problemset/problem/208/A

import io
import os
import sys
import re

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

print(re.sub(r'(WUB)+', ' ', inp().decode()).strip())
