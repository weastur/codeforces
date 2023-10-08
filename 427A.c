#include <stdio.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

int main() {
    int n, x;
    int ans = 0;
    int cur = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        cur += x;
        if (cur < 0) {
            ans = MIN(ans, cur);
        }
    }
    ans *= -1;
    printf("%d\n", ans);
}
