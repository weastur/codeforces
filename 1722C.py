# URL: https://codeforces.com/problemset/problem/1722/C

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = set(map(lambda x: x.decode(), inp().split()))
    b = set(map(lambda x: x.decode(), inp().split()))
    c = set(map(lambda x: x.decode(), inp().split()))
    aa = len(a - b - c) * 3 + len(a & b) + len(a & c) - len(a & b & c) * 2
    bb = len(b - a - c) * 3 + len(b & a) + len(b & c) - len(a & b & c) * 2
    cc = len(c - b - a) * 3 + len(c & a) + len(c & b) - len(a & b & c) * 2
    out(f"{aa} {bb} {cc}\n")
