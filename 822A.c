#include <stdio.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

int a, b;

int main() {
    scanf("%d%d", &a, &b);
    int c = MIN(a, b);
    int ans = 1;
    for (int i = 1; i <= c; i++)
        ans *= i;
    printf("%d", ans);
}
