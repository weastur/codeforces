# URL: https://codeforces.com/problemset/problem/677/A
n, h = map(int, input().split())
ans = n
for a in map(int, input().split()):
    ans += a > h
print(ans)
