import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
a = list(map(int, inp().split()))
m = [0] * n
for i in range(n):
    m[i] = a[i] % 2
pos = m.index(0) if sum(m) > 1 else m.index(1)
print(pos + 1)
