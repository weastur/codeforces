#include <stdio.h>
#include <string.h>

#define N 101

int t, pre[N];
char s[N];

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        scanf("%s", s);
        size_t n = strlen(s);
        pre[0] = -1;
        for (size_t i = 1; i < n; i++) {
            if (s[i - 1] == '1') {
                pre[i] = i - 1;
            } else {
                pre[i] = pre[i - 1];
            }
        }
        int ans = 0;
        for (size_t i = 0; i < n; i++) {
            if (s[i] == '1' && pre[i] != -1) {
                ans += i - pre[i] - 1;
            }
        }
        printf("%d\n", ans);
    }
}
