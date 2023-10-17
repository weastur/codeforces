#include <stdio.h>

int t, a, b, c;

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d", &a, &b, &c);
        if (a > b || (a == b && c % 2)) {
            puts("First");
        } else {
            puts("Second");
        }
    }
}
