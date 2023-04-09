t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().split()))
    x, y, x1, y1, x2, y2 = list(map(int, input().split()))
    if x == x1 and x == x2 and (a > 0 or b > 0):
        print("No")
        continue
    elif y == y1 and y == y2 and (c > 0 or d > 0):
        print("No")
        continue
    else:
        if a > b and a - b > x - x1:
            print("No")
            continue
        elif b - a > x2 - x:
            print("No")
            continue
        if c > d and c - d > y - y1:
            print("No")
            continue
        elif d - c > y2 - y:
            print("No")
            continue
    print("Yes")
