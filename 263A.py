# URL: https://codeforces.com/problemset/problem/263/A
for i in range(5):
    row = input().split()
    j = -1
    try:
        j = row.index('1')
    except ValueError:
        pass
    if j != -1:
        print(abs(2 - i) + abs(2 - j))
        break
