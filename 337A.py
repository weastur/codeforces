import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n, m = map(int, inp().split())
a = list(map(int, inp().split()))
a.sort()
print(min(a[x] - a[x - n + 1] for x in range(n - 1, m)))
