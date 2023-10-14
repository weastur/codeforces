# URL: https://codeforces.com/problemset/problem/1607/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

d = {}
for _ in range(int(inp())):
    t, s = inp(), inp()
    for i in range(len(t)):
        d[t[i]] = i
    ans = 0
    pre = d[s[0]]
    for i in range(len(s)):
        ans += abs(pre - d[s[i]])
        pre = d[s[i]]
    out(f"{ans}\n")
