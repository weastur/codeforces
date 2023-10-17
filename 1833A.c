#include <stdio.h>
#include <stdbool.h>

#define N 51

int t, n, ans;
char s[N];

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d\n%s", &n, s);
        ans = 0;
        for (size_t i = 1; i < n; i++) {
            bool found = false;
            for (size_t j = 1; j < i; j++) {
                if (s[j - 1] == s[i - 1] && s[j] == s[i]) {
                    found = true;
                    break;
                }
            }
            ans += !found;
        }
        printf("%d\n", ans);
    }
}
