#include <stdio.h>

int main() {
  int n, m, a;
  scanf("%d%d%d", &n, &m, &a);
  printf("%lld\n", ((n + a - 1) / a) * 1LL * ((m + a - 1) / a));
  return 0;
}