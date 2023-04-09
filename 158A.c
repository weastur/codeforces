#include <stdio.h>

#define N 101

int main() {
  int n, k, x, pre, ans = 0;
  scanf("%d%d", &n, &k);
  for (size_t i = 0; i < n; i++) {
    scanf("%d", &x);
    if (x <= 0 || (i + 1 > k && pre != x)) {
      break;
    }
    ans++;
    pre = x;
  }
  printf("%d\n", ans);
  return 0;
}