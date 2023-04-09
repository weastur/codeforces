#!/usr/bin/env pypy3

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = 0
    ans = 0
    i = 0
    while i < n:
        s += a[i]
        if s / (i + 1) < x:
            break
        i += 1
    print(i)
