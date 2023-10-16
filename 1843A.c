#include <stdio.h>
#include <stdlib.h>

#define N 50


int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int t, n, l, r, ans, a[N];

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", a + i);
        qsort(a, n, sizeof(a[0]), cmp);
        ans = 0;
        l = 0;
        r = n - 1;
        while (r - l >= 1) {
            ans += a[r] - a[l];
            r--;
            l++;
        }
        printf("%d\n", ans);
    }
}
