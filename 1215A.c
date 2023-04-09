#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
  int a1, a2, k1, k2, n, ans1, ans2;
  scanf("%d%d%d%d%d", &a1, &a2, &k1, &k2, &n);
  int d = (k1 - 1) * a1 + (k2 - 1) * a2;
  if (d >= n) {
    ans1 = 0;
  } else {
    ans1 = n - d;
  }
  if (k1 > k2) {
    int t = k1;
    k1 = k2;
    k2 = t;
    t = a1;
    a1 = a2;
    a2 = t;
  }
  int d2 = a1 * k1;
  if (d2 >= n) {
    ans2 = n / k1;
  } else {
    ans2 = a1 + (n - d2) / k2;
  }
  printf("%d %d", ans1, ans2);
  return 0;
}