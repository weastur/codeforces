#include <stdio.h>

int main() {
    int n, k;
    scanf("%d%d", &n, &k);
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        if (5 * ((i * (i + 1)) / 2) + k <= 240) {
            ans = i;
        } else {
            break;
        }
    }
    printf("%d\n", ans);
}
