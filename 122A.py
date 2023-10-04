# URL: https://codeforces.com/problemset/problem/122/A
n = int(input())
for x in range(4, n + 1):
    if n % x == 0 and not (set(str(x)) - {'4', '7'}):
        print("YES")
        break
else:
    print("NO")
