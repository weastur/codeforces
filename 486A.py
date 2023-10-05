# URL: https://codeforces.com/problemset/problem/486/A

n = int(input())
ans = (n + 1) // 2
if n % 2 == 1:
    ans *= -1
print(ans)
