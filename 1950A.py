#!/usr/bin/env pypy3.10

import io
import os
import sys

if "LOCAL" not in os.environ:
    input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
    inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
else:
    inp = input
out = []

for _ in range(int(inp())):
    a, b, c = map(int, inp().split())
    if a < b < c:
        out.append("STAIR")
    elif a < b and b > c:
        out.append("PEAK")
    else:
        out.append("NONE")

sys.stdout.write("\n".join(map(str, out)))
