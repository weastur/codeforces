#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n, m, k;
        scanf("%d%d%d", &n, &m, &k);
        if (k == (n - 1) + (m - 1) * n) {
            puts("YES");
        } else {
            puts("NO");
        }
    }
}
