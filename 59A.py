# URL: https://codeforces.com/problemset/problem/59/A
s = input()
l = sum(map(lambda ch: ch.islower(), s))
r = sum(map(lambda ch: ch.isupper(), s))
print(s.lower() if l >= r else s.upper())
