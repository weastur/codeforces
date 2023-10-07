import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n = int(inp())
h, a = [0] * n, [0] * n
for i in range(n):
    h[i], a[i] = map(int, inp().split())
ans = 0
for i in range(n):
    ans += a.count(h[i])
print(ans)
