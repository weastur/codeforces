# URL: https://codeforces.com/problemset/problem/266/B
n, t = map(int, input().split())
line = list(input())
for _ in range(t):
    pos = 0
    while pos < n:
        if pos + 1 < n and line[pos] == 'B' and line[pos + 1] == 'G':
            line[pos], line[pos + 1] = 'G', 'B'
            pos += 2
        else:
            pos += 1

print(''.join(line))
