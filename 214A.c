#include <stdio.h>

#define N 1000

int main() {
    int ans, n, m;
    ans = 0;
    scanf("%d%d", &n, &m);
    for (int a=0; a<=N; a++) {
        for (int b=0; b<=N; b++) {
            int c = a * a + b;
            if (c == n) {
                ans += (b * b + a == m);
            } else if (c > n) {
                continue;
            }
        }
    }
    printf("%d", ans);
}
