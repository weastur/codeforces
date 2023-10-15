# URL: https://codeforces.com/problemset/problem/1703/C

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    a = list(map(int, inp().split()))
    b = []
    for _ in range(n):
        _, x = inp().split()
        b.append(x.decode())
    for i in range(n):
        for e in b[i][::-1]:
            if e == 'U':
                a[i] -= 1
                if a[i] < 0:
                    a[i] = 9
            else:
                a[i] += 1
                if a[i] > 9:
                    a[i] = 0
    out(" ".join(map(str, a)) + "\n")
