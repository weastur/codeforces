import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
ans = 0
for x in (100, 20, 10, 5, 1):
    ans += n // x
    n %= x
print(ans)
