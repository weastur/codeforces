#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 300500

int t, n;
long long sum, sum2, ans, a[N], b[N], c[N];

long long min(long long a, long long b) {
  if (a < b) {
    return a;
  } else {
    return b;
  }
}

int main(int argc, const char *argv[]) {
  scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);
    sum = 0;
    sum2 = 0;
    for (size_t i = 0; i < n; ++i) {
      scanf("%lld%lld", a + i, b + i);
      sum += a[i];
    }
    for (size_t i = 0; i < n; ++i) {
      if (i == 0) {
        c[i] = min(b[n - 1], a[i]);
      } else {
        c[i] = min(b[i - 1], a[i]);
      }
      sum2 += c[i];
    }
    ans = 1000000000000000000L;
    for (size_t i = 0; i < n; ++i) {
      ans = min(ans, sum - sum2 + c[i]);
    }
    printf("%lld\n", ans);
  }
  return 0;
}
