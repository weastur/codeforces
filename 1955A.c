#include <stdio.h>

int t, a, b, n, ans;

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d", &n, &a, &b);
        if (a * 2 <= b) {
            ans = n * a;
        } else {
            ans = (n / 2) * b + (n % 2) * a;
        }
        printf("%d\n", ans);
    }

}
