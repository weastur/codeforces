# URL: https://codeforces.com/problemset/problem/136/A
n = int(input())
p = list(map(int, input().split()))
ans = p.copy()
for i in range(1, n + 1):
    ans[p[i - 1] - 1] = i
print(" ".join(map(str, ans)))
