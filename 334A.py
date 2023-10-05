# URL: https://codeforces.com/problemset/problem/344/A
import io
import os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

pre = 'XX'
ans = 0
for _ in range(int(input())):
    cur = input()
    if cur != pre:
        ans += 1
    pre = cur
print(ans)
