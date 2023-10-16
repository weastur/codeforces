#include <stdio.h>

int n, t;

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        int m = n % 7;
        int ld = n % 10;
        if (ld >= m)
            printf("%d\n", n - m);
        else if (ld + 7 - m < 10)
            printf("%d\n", n + 7 - m);
    }
}
