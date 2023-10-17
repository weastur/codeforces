#include <stdio.h>

int t, a, b, c, x, y;

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d%d%d", &a, &b, &c, &x, &y);
        x = a <= x ? x - a : 0;
        y = b <= y ? y - b : 0;
        if (x + y - c <= 0) {
            puts("YES");
        } else {
            puts("NO");
        }
    }
}
