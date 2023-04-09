#include <stdio.h>

#define MOD 1000000007
#define N 1010

char a[N][N];
int h, w, r, c, cnt;

long long pow2(long long a, int n) {
  long long ans = 1;
  while (n) {
    if (n & 1) ans = (ans * a) % MOD;
    a = (a * a) % MOD;
    n >>= 1;
  }
  return ans;
}

int main() {
  scanf("%d%d", &h, &w);
  for (int i = 1; i <= h; ++i)
    for (int j = 1; j <= w; ++j) a[i][j] = -1;
  for (int i = 1; i <= h; i++) {
    scanf("%d", &r);
    for (int j = 1; j <= r; ++j) a[i][j] = 1;
    a[i][r + 1] = 0;
  }
  for (int j = 1; j <= w; j++) {
    scanf("%d", &c);
    for (int i = 1; i <= c; ++i) {
      if (a[i][j] != 0)
        a[i][j] = 1;
      else {
        printf("0");
        return 0;
      }
    }
    if (a[c + 1][j] != 1)
      a[c + 1][j] = 0;
    else {
      printf("0");
      return 0;
    }
  }
  for (int i = 1; i <= h; ++i) {
    for (int j = 1; j <= w; ++j) {
      if (a[i][j] == -1) cnt++;
    }
  }
  printf("%lld\n", pow2(2, cnt));
  return 0;
}