# URL: https://codeforces.com/problemset/problem/1547/B

import io
import os
import sys
import string

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

t = string.ascii_lowercase
for _ in range(int(inp())):
    s = inp().decode()
    x = s.find('a')
    if x == -1:
        out("NO\n")
    else:
        p = 1
        l = x - 1
        r = x + 1
        while l >= 0 or r < len(s):
            if l >= 0 and s[l] == t[p]:
                p += 1
                l -= 1
            elif r < len(s) and s[r] == t[p]:
                p += 1
                r += 1
            else:
                out("NO\n")
                break
        else:
            out("YES\n")
