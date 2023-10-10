# URL: https://codeforces.com/problemset/problem/1343/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    n = int(inp())
    if n % 4:
        out("NO\n")
    else:
        out("YES\n")
        a = [2 * i for i in range(1, n // 2 + 1)]
        a.extend(2 * i + 1 for i in range(n // 2))
        a[n - 1] += n // 2
        out(" ".join(map(str, a)) + "\n")
