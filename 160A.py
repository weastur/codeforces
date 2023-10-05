# URL: https://codeforces.com/problemset/problem/160/A
_ = input()
a = list(map(int, input().split()))
a.sort(reverse=True)
total = sum(a)
s = 0
for i in range(1, len(a) + 1):
    s += a[i - 1]
    if s > total - s:
        print(i)
        break
