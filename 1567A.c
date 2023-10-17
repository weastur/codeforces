#include <stdio.h>

#define N 101

int t, n;
char s[N];

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d\n%s", &n, s);
        for (size_t i = 0; i < n; i++) {
            if (s[i] == 'U') {
                s[i] = 'D';
            } else if (s[i] == 'D') {
                s[i] = 'U';
            }
        }
        puts(s);
    }
}
