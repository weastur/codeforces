# URL: https://codeforces.com/problemset/problem/1743/A

import io
import os
import sys
import itertools

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

s = set(range(10))
for _ in range(int(inp())):
    n = int(inp())
    a = list(s - set(map(int, inp().split())))
    ans = 0
    for c in itertools.combinations(a, 2):
        k = sum(c) * 2
        for r in itertools.product(c, repeat=4):
            ans += sum(r) == k
    out(f"{ans}\n")
