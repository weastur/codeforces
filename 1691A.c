#include <stdio.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

int t, n, a, cnt;

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        cnt = 0;
        for (size_t i = 0; i < n; i++) {
            scanf("%d", &a);
            cnt += a % 2;
        }
        int ans = MIN(cnt, n - cnt);
        printf("%d\n", ans);
    }
}
