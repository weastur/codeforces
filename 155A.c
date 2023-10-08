#include <stdio.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int main() {
    int n, x, min, max, nmax, nmin;
    int ans = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        if (!i) {
            max = x;
            min = x;
        } else {
            nmax = MAX(max, x);
            nmin = MIN(min, x);
            if (nmax != max || nmin != min) {
                ans++;
                max = nmax;
                min = nmin;
            }
        }
    }
    printf("%d\n", ans);
}
