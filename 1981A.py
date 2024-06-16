import io
import math
import os
import platform
import sys

if platform.system() != "Darwin":
    input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
    inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
else:
    inp = input
out = []

for _ in range(int(inp())):
    _, r = map(int, inp().split())
    out.append(int(math.log2(r)))

sys.stdout.write("\n".join(map(str, out)))
