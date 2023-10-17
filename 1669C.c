#include <stdio.h>
#include <stdbool.h>

#define N 50

int main() {
    int t, n, a[N];
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (size_t i = 0; i < n; i++) {
            scanf("%d", a + i);
        }
        bool ans = true;
        for (size_t i = 2; i < n; i++) {
            if ((i % 2 == 0 && a[0] % 2 != a[i] % 2) || (i % 2 == 1 && a[1] % 2 != a[i] % 2)) {
                ans = false;
                break;
            }
        }
        if (ans) {
            puts("YES");
        } else {
            puts("NO");
        }
    }
}
