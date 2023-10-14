# URL: https://codeforces.com/problemset/problem/1790/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

pi = '314159265358979323846264338327'
for _ in range(int(inp())):
    t = inp().decode()
    ans = 0
    for i in range(len(t)):
        if t[i] == pi[i]:
            ans = i + 1
        else:
            break
    out(f"{ans}\n")
