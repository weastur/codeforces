#include <stdio.h>

#define N 200000

int t, n, s, k, cnt, a[N];

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        s = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", a + i);
            s += a[i];
        }
        if (s % n != 0) {
            printf("-1\n");
            continue;
        }
        cnt = s / n;
        k = 0;
        for (int i = 0; i < n; i++)
            k += a[i] > cnt;
        printf("%d\n", k);
    }
}
