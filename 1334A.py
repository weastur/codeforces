#!/usr/bin/env pypy3

t = int(input())
for _ in range(t):
    n = int(input())
    p, c = [], []
    ans = True
    for _ in range(n):
        pp, cc = map(int, input().split())
        p.append(pp)
        c.append(cc)
        if cc > pp:
            ans = False
        if len(p) > 1:
            dp = p[-1] - p[-2]
            dc = c[-1] - c[-2]
            if dp < 0 or dc < 0 or dp < dc:
                ans = False
    if ans:
        print("YES")
    else:
        print("NO")
