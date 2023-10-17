#include <stdio.h>

#define MAX 101

int t, n, a, m, c;

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        m = MAX;
        c = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &a);
            if (a < m) {
                m = a;
                c = 1;
            } else if (a == m) {
                c++;
            }
        }
        printf("%d\n", n - c);
    }
}
