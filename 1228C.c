#include <stdio.h>

#define MOD 1000000007
#define N 100500

long long x, n, ans, m, prime[N];
;

long long min(long long a, long long b) {
  if (a < b) return a;
  return b;
}

long long ppow(long long a, long long n) {
  long long res = 1;
  while (n) {
    if (n & 1) res = (res * a) % MOD;
    a = (a * a) % MOD;
    n >>= 1;
  }
  return res;
}

int main() {
  scanf("%lld%lld", &x, &n);
  for (long long i = 2; i * i <= x; i++) {
    if (x % i == 0) prime[m++] = i;
    while (x % i == 0) {
      x /= i;
    }
  }
  if (x > 1) prime[m++] = x;
  ans = 1;
  for (int i = 0; i < m; i++) {
    long long j = prime[i];
    while (1) {
      long long m = n / j;
      ans = (ans * ppow(j % MOD, m - m / prime[i])) % MOD;
      if (n / j < prime[i]) break;
      j *= prime[i];
    }
  }
  printf("%lld", ans);
  return 0;
}