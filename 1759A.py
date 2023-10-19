# URL: https://codeforces.com/problemset/problem/1759/A

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

for _ in range(int(inp())):
    s = inp().decode()
    if s[0] == 'e':
        s = 'Y' + s
    elif s[0] == 's':
        s = 'Ye' + s
    if s[-1] == 'Y':
        s = s + 'es'
    elif s[-1] == 'e':
        s = s + 's'
    n = len(s)
    if n % 3 != 0 or 'Yes' * (n // 3) != s:
        out("NO\n")
    else:
        out("YES\n")
