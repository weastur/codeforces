#include <stdio.h>
#include <string.h>

int t, s, n, m;

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &s);
        m = 0;
        for (int i = 9; i > 0 && s; i--) {
            if (s >= i) {
                m = m * 10 + i;
                s -= i;
            }
        }
        n = 0;
        while (m) {
            n = n * 10 + m % 10;
            m /= 10;
        }
        printf("%d\n", n);
    }
}
