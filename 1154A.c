#include <stdio.h>

int max4(int x1, int x2, int x3, int x4) {
    int d1 = x1 > x2 ? x1 : x2;
    int d2 = x3 > x4 ? x3 : x4;
    return d1 > d2 ? d1 : d2;
}

int x1, x2, x3, x4, a, b, c;

int main() {
    scanf("%d%d%d%d", &x1, &x2, &x3, &x4);
    int sum = max4(x1, x2, x3, x4);
    if (x1 != sum)
        printf("%d ", sum - x1);
    if (x2 != sum)
        printf("%d ", sum - x2);
    if (x3 != sum)
        printf("%d ", sum - x3);
    if (x4 != sum)
        printf("%d ", sum - x4);
}
