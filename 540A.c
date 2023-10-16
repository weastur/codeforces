#include <stdio.h>
#include <string.h>

#define N 1001
#define ABS(x) ((x) < 0 ? ((-1) * (x)) : (x))

int n, ans;
char s[N], t[N];

int main() {
    scanf("%d\n%s\n%s", &n, s, t);
    for (int i = 0; i < n; i++) {
        int x = ABS(s[i] - t[i]);
        if (x > 5)
            x = 10 - x;
        ans += x;
    }
    printf("%d", ans);
}
