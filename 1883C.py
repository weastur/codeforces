# URL: https://codeforces.com/contest/1883/problem/C

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write


def rint():
    return int(inp())


def rints():
    return map(int, inp().split())


def rlist():
    return list(rints())


for _ in range(int(inp())):
    n, k = rints()
    a = rlist()
    if k == 4:
        cnt = 0
        cnt2 = 0
        for x in a:
            cnt += x % 2 == 0
            cnt2 += x % 4 == 0
        if cnt >= 2 or cnt2 != 0:
            ans = 0
        elif cnt == 1:
            ans = 1 if n > 1 else 4 - a[0] % 4
        elif cnt == 0:
            if a.count(3) + a.count(7):
                ans = 1
            else:
                ans = 2 if n > 1 else 4 - a[0] % 4
    else:
        b = [a[i] % k for i in range(n)]
        ans = k - max(b) if b.count(0) == 0 else 0
    out(f"{ans}\n")
