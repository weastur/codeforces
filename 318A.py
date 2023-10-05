# URL: https://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())
m = (n + 1) // 2
if k <= m:
    print(2 * k - 1)
else:
    print(2 * (k - m))
