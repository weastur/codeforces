#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        int ans;
        if (n == 1) {
            ans = 2;
        } else if (n % 3 == 0) {
            ans = n / 3;
        } else {
            ans = n / 3 + 1;
        }
        printf("%d\n", ans);
    }
}
