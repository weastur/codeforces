# URL: https://codeforces.com/problemset/problem/58/A
w = ['h', 'e', 'l', 'l', 'o']
for ch in input():
    if w[0] == ch:
        w.pop(0)
    if not w:
        print("YES")
        break
else:
    print("NO")
