# URL: https://codeforces.com/problemset/problem/1807/C

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    s = inp().decode()
    d = {}
    for i, x in enumerate(s):
        if i == 0:
            d[x] = 0
            continue
        if s[i] == s[i - 1]:
            out("NO\n")
            break
        elif x not in d:
            d[x] = 1 - d[s[i - 1]]
        elif d[s[i - 1]] == d[x]:
            out('NO\n')
            break
    else:
        out("YES\n")
