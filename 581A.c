#include <stdio.h>

int a, b, x, y;

int main() {
    scanf("%d%d", &a, &b);
    x = a < b ? a : b;
    a -= x;
    b -= x;
    y = a / 2 + b / 2;
    printf("%d %d\n", x, y);
}
