n, m = map(int, input().split())
l = list(map(int, input().split()))
p = []
for i in range(m):
    if l[i] > n - i:
        print(-1)
        exit(0)
    p.append(i + 1)
last = n
for i in range(m - 1, -1, -1):
    if p[i] + l[i] - 1 >= last:
        break
    p[i] = last - l[i] + 1
    last = p[i] - 1
if p[0] > 1:
    print(-1)
else:
    print(" ".join(str(elem) for elem in p))
