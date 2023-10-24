# URL: https://codeforces.com/problemset/problem/1674/B

import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = []

for _ in range(int(inp())):
    s = inp().decode()
    ans = (ord(s[0]) - ord('a')) * 25 + ord(s[1]) - ord('a') + (s[1] < s[0])
    out.append(str(ans))

sys.stdout.write("\n".join(out))
