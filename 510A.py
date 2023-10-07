import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

n, m = map(int, inp().split())
for i in range(1, n + 1):
    if i % 2 == 1:
        out('#' * m + '\n')
    elif i % 4 == 0:
        out('#' + '.' * (m - 1) + '\n')
    else:
        out('.' * (m - 1) + '#' + '\n')
