#!/usr/bin/env pypy3

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mmin, mmax = -1, -1
    for i in range(n):
        if b[i] < a[i] and mmin == -1:
            mmin = i
        if b[i] > a[i] and mmax == -1:
            mmax = i
    found_mmin = mmin == -1
    found_mmax = mmax == -1
    for i in range(n):
        if a[i] == 1 and i < mmax:
            found_mmax = True
        elif a[i] == -1 and i < mmin:
            found_mmin = True
        if (a[i] < b[i] and not found_mmax) or (a[i] > b[i] and not found_mmin):
            break
    if found_mmax and found_mmin:
        print("YES")
    else:
        print("NO")
