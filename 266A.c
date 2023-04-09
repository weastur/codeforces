#include <stdio.h>

#define N 100

int n, ans;
char s[N];

int main() {
  scanf("%d\n%s", &n, s);
  for (int i = 1; i < n; i++) {
    ans += s[i] == s[i - 1];
  }
  printf("%d\n", ans);
  return 0;
}