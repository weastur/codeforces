#include <stdio.h>

int k, r;

int main() {
    scanf("%d%d", &k, &r);
    for (int ans = 1; ans <= 10; ans++) {
        int d = (k * ans) % 10;
        if (!d || d == r) {
            printf("%d", ans);
            break;
        }
    }
}
