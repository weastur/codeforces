import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

d = {}
for _ in range(int(inp())):
    s = inp().decode()
    if s not in d:
        d[s] = 0
        out('OK\n')
    else:
        last = d[s]
        d[s] += 1
        new = s + str(last + 1)
        d[new] = 0
        print(new)
