#include <stdio.h>
#include <string.h>

#define N 101

int main() {
    char s[N], t[N];
    int ans = 0;
    scanf("%s", s);
    int n = strlen(s);
    for (int i = 0; i < n - 2; i++)
        for (int j = i + 1; j < n - 1; j++)
            for (int k = j + 1; k < n; k++)
                if (s[i] == 'Q' && s[j] == 'A' && s[k] == 'Q')
                    ans++;
    printf("%d", ans);
}
