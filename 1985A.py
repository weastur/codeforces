import io
import os
import sys

inp = input
out = []
if "LOCAL" not in os.environ:
    input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
    inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")  # noqa

for _ in range(int(inp())):
    a, b = map(lambda s: s.decode(), inp().split())
    out.append(b[0] + a[1:] + " " + a[0] + b[1:])

sys.stdout.write("\n".join(map(str, out)))
