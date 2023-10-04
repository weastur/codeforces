# URL: https://codeforces.com/problemset/problem/116/A
ans, cur = 0, 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    cur += (-1 * a) + b
    ans = max(ans, cur)
print(ans)
