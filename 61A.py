# URL: https://codeforces.com/problemset/problem/61/A
a = input()
b = input()
x = int(a, 2)
y = int(b, 2)
print(f'{x^y:b}'.zfill(len(a)))
