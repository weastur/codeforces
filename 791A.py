# URL: https://codeforces.com/problemset/problem/791/A

a, b = map(int, input().split())
ans = 0
while a <= b:
    ans += 1
    a *= 3
    b *= 2
print(ans)