# URL: https://codeforces.com/problemset/problem/1772/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write


def check(a):
    return a[0][0] < a[0][1] and a[0][0] < a[1][0] and a[1][0] < a[1][1] and a[
        0][1] < a[1][1]


for _ in range(int(inp())):
    a, b = map(int, inp().split())
    c, d = map(int, inp().split())
    aa = [[a, b], [c, d]]
    bb = [[c, a], [d, b]]
    cc = [[d, c], [b, a]]
    dd = [[b, d], [a, c]]
    if check(aa) or check(bb) or check(cc) or check(dd):
        out("YES\n")
    else:
        out("NO\n")
