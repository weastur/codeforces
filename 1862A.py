# URL: https://codeforces.com/problemset/problem/1862/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n, m = map(int, inp().split())
    s = [[] for _ in range(n)]
    v, i, k, a = False, False, False, False
    for j in range(n):
        s[j].extend(inp().decode())
    for y in range(m):
        for x in range(n):
            if not v and s[x][y] == 'v':
                v = True
                break
            if v and not i and s[x][y] == 'i':
                i = True
                break
            if v and i and not k and s[x][y] == 'k':
                k = True
                break
            if v and i and k and not a and s[x][y] == 'a':
                a = True
                break
    if all((v, i, k, a)):
        out("YES\n")
    else:
        out("NO\n")
