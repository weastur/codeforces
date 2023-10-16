#include <stdio.h>
#include <string.h>

#define A 10001

int t, n, a, ans, m;
char b[A];

int main() {
    scanf("%d", &t);
    while (t--) {
        m = 0;
        memset(b, 0, sizeof b);
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a);
            m += b[a];
            b[a] = 1;
        }
        ans = n - m - m % 2;
        printf("%d\n", ans);
    }
}
