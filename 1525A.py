# URL: https://codeforces.com/problemset/problem/1525/A

import io
import os
import sys
import math

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = []

def rint():
    return int(inp())

def rints():
    return map(int, inp().split())

def rlist():
    return list(rints())

for _ in range(int(inp())):
    k = rint()
    ans = 100
    ans //= math.gcd(k, ans)
    out.append(f"{ans}")

sys.stdout.write("\n".join(out))
