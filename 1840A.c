#include <stdio.h>

#define N 101

int t, n, m, p;
char s[N], a[N];

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d\n%s", &n, s);
        m = 0;
        p = 0;
        while (p < n) {
            a[m++] = s[p];
            char ch = s[p++];
            while (p < n && s[p++] != ch)
                ;
        }
        a[m] = '\0';
        puts(a);
    }
}
