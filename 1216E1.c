#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 22000
#define M 11

int q, k, a[N + 1], b[N + 1];
char snum[M];

int count(int n) {
  int ans = 0;
  while (n) {
    ans++;
    n = n / 10;
  }
  return ans;
}

char c_pos(int n, int pos) {
  memset(snum, 0, M);
  sprintf(snum, "%d", n);
  return snum[pos - 1];
}

int main() {
  a[1] = 1;
  b[1] = 1;
  for (int i = 2; i <= N; i++) {
    b[i] = b[i - 1] + count(i);
    a[i] = a[i - 1] + b[i];
  }
  scanf("%d", &q);
  for (int i = 0; i < q; ++i) {
    scanf("%d", &k);
    for (int j = 1; j <= N; j++) {
      if (a[j] >= k) {
        int kk = k - a[j - 1];
        for (int t = 1; t <= j; t++) {
          if (kk <= b[t]) {
            printf("%c\n", c_pos(t, kk - b[t - 1]));
            break;
          }
        }
        break;
      }
    }
  }
  return 0;
}