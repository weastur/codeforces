#!/usr/bin/env pypy3

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    for i in range(n - 1):
        print("B" * m)
    print("B" * (m - 1) + "W")
