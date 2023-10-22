# URL: https://codeforces.com/contest/1884/problem/B

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
    n = rint()
    a = list(map(int, inp().decode()))
    cur = 0
    last = n
    ans = []
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            ans.append(cur)
        else:
            found = False
            for j in range(min(last - 1, i), -1, -1):
                if a[j] == 0:
                    last = j
                    found = True
                    break
            if found:
                cur += i - last
                a[i] = 0
                a[last] = 1
                ans.append(cur)
            else:
                last = 0
                ans.append(-1)
    out(" ".join(map(str, ans)) + "\n")
