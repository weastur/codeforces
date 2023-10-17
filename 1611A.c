#include <stdio.h>
#include <string.h>

#define N 11

int t, p, l, ans;
char s[N];

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%s", s);
        l = strlen(s);
        if ((s[l - 1] - '0') % 2 == 0)
            ans = 0;
        else if ((s[0] - '0') % 2 == 0)
            ans = 1;
        else {
            p = -1;
            for (size_t i = 0; i < l; i++) {
                if ((s[i] - '0') % 2 == 0) {
                    p = i;
                }
            }
            ans = p == -1 ? -1 : 2;
        }
        printf("%d\n", ans);
    }
}
