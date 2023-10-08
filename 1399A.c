#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define N 101

int t, n, a, d[N];

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        memset(d, 0, sizeof d);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a);
            d[a]++;
        }
        int cur = 0;
        bool found = false;
        for (int i = 0; i < N; i++) {
            cur += d[i];
            found |= !d[i] && cur && cur != n;
        }
        if (!found) {
            puts("YES");
        } else {
            puts("NO");
        }
    }
}
