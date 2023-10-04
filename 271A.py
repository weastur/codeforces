# URL: https://codeforces.com/problemset/problem/271/A
for ans in range(int(input()) + 1, 9013):
    if len(set(str(ans))) == 4:
        print(ans)
        break
