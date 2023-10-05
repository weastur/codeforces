# URL: https://codeforces.com/problemset/problem/705/A

print("I hate", end="")
for i in range(2, int(input()) + 1):
    if i % 2 == 0:
        print(" that I love", end="")
    else:
        print(" that I hate", end="")
print(" it")
