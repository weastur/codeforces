#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        long long n, m, x;
        scanf("%lld%lld%lld", &n, &m, &x);
        long long c = (x + n - 1) / n;
        long long r = x - n * (c - 1);
        long long y = (r - 1) * m + c;
        printf("%lld\n", y);
    }
}
