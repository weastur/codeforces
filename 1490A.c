#include <stdio.h>

int t, n, a, pre, x, y, ans;

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        a = -1;
        ans = 0;
        while (n--) {
            pre = a;
            scanf("%d", &a);
            if (pre == -1) {
                continue;
            }
            x = pre;
            y = a;
            if (a < pre) {
                x = a;
                y = pre;
            }
            while (x * 2 < y) {
                x *= 2;
                ans++;
            }
        }
        printf("%d\n", ans);
    }
}
