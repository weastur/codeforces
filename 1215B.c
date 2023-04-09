#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 200500
#define M 2

int n, a;
long long ans1, ans2, f[N][M];

int main(int argc, char *argv[]) {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a);
    if (i == 0) {
      if (a < 0) {
        f[i][0] = 1;
      } else {
        f[i][1] = 1;
      }
    } else {
      if (a < 0) {
        f[i][0] = f[i - 1][1] + 1;
        f[i][1] = f[i - 1][0];
      } else {
        f[i][0] = f[i - 1][0];
        f[i][1] = f[i - 1][1] + 1;
      }
    }
    ans1 += f[i][0];
    ans2 += f[i][1];
  }
  printf("%lld %lld", ans1, ans2);

  return 0;
}