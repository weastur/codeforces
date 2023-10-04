# URL: https://codeforces.com/problemset/problem/734/A
n = int(input())
a = input().count('A')
d = n - a
if a > d:
    print("Anton")
elif a == d:
    print("Friendship")
else:
    print("Danik")
