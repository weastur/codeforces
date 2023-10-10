# URL: https://codeforces.com/problemset/problem/1360/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    _ = inp()
    s = list(map(int, inp().split()))
    s.sort()
    ans = s[-1]
    for i in range(1, len(s)):
        ans = min(ans, s[i] - s[i - 1])
    out(f"{ans}\n")
