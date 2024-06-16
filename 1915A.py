import io
import os
import sys

if "DEBUG" not in os.environ:
    input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
    inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
else:
    inp = input
out = []

for _ in range(int(inp())):
    a, b, c = map(int, inp().split())
    if a == b:
        ans = c
    elif a == c:
        ans = b
    else:
        ans = a
    out.append(ans)

sys.stdout.write("\n".join(map(str, out)))
