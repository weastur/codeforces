#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 200500

int x, z, n, max, a[N];
long long y;

int gcd(int a, int b) {
  if (b == 0)
    return a;
  else
    return gcd(b, a % b);
}

int main(int argc, char *argv[]) {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", a + i);
    if (i == 0) {
      max = a[i];
    } else {
      if (a[i] > max) {
        max = a[i];
      }
    }
  }
  for (int i = 0; i < n; i++) z = gcd(z, max - a[i]);
  for (int i = 0; i < n; i++) y += (max - a[i]) / z;
  printf("%lld %d", y, z);
  return 0;
}