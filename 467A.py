# URL: https://codeforces.com/problemset/problem/467/A
ans = 0
for _ in range(int(input())):
    p, q = map(int, input().split())
    ans += (q - p) >= 2
print(ans)
