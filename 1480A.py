# URL: https://codeforces.com/problemset/problem/1480/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    s = inp().decode()
    t = []
    st = 0
    for x in s:
        if st == 0:
            if x == 'a':
                t.append('b')
            else:
                t.append('a')
        else:
            if x == 'z':
                t.append('y')
            else:
                t.append('z')
        st = 1 - st
    out(''.join(t) + '\n')
