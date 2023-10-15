# URL: https://codeforces.com/problemset/problem/1760/C

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    s = list(map(int, inp().split()))
    m1, m2 = 0, 1
    for i in range(1, n):
        if s[m1] < s[i]:
            m2 = m1
            m1 = i
        elif s[m2] < s[i]:
            m2 = i
    ans = []
    for i in range(n):
        if m1 != i:
            ans.append(s[i] - s[m1])
        else:
            ans.append(s[i] - s[m2])
    out(" ".join(map(str, ans)) + "\n")
