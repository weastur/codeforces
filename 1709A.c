#include <stdio.h>

int t, x, a[4];

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d%d", &x, a + 1, a + 2, a + 3);
        if (a[x] && a[a[x]]) {
            puts("YES");
        } else {
            puts("NO");
        }
    }
}

