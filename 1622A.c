#include <stdio.h>

int a, b, c, t;

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d", &a, &b, &c);
        if ((a == b && c % 2 == 0) || (a == c && b % 2 == 0) || (b == c && a % 2 == 0)) {
            puts("YES");
        } else if (a + b == c || a + c == b || b + c == a) {
            puts("YES");
        } else {
            puts("NO");
        }
    }
}
