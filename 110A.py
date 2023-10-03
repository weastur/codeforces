# URL: https://codeforces.com/problemset/problem/110/A

n = input()
cnt = n.count("4") + n.count("7")
print("YES" if cnt == 4 or cnt == 7 else "NO")
