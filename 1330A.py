#!/usr/bin/env pypy3

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(1, 301):
        if i in a:
            continue
        if x:
            x -= 1
            continue
        print(i - 1 + x)
        break
