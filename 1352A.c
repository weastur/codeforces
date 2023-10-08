#include <stdio.h>

int t, n, k, a[4];

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        k = 0;
        int zero = 0;
        while (n) {
            if (n % 10 == 0) {
                n /= 10;
                zero++;
                continue;
            } else {
                a[k++] = n % 10;
                for (int i = 0; i < zero; i++)
                    a[k - 1] *= 10;
                zero++;
                n /= 10;
            }
        }
        printf("%d\n", k);
        for (int i = 0; i < k; i++)
            printf("%d ", a[i]);
        printf("\n");
    }
}
