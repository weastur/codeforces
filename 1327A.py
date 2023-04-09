#!/usr/bin/env pypy3

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k % 2 != n % 2 or k * k > n:
        print("NO")
    else:
        print("YES")
