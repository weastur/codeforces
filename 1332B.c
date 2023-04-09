#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 1001
#define M 12

int gcd(int a, int b) {
  if (b == 0)
    return a;
  else
    return gcd(b, a % b);
}

char is_prime(int a) {
  int d = 2;
  while (d * d <= a) {
    if (a % d == 0) {
      return 0;
    }
    d++;
  }
  return 1;
}

int t, n, m, a[N], b[N], c[M], d[M];

int main(int argc, const char *argv[]) {
  scanf("%d\n", &t);
  int current_color = 1;
  for (int i = 4; i < N; ++i) {
    if (b[i] || is_prime(i)) {
      continue;
    }
    b[i] = current_color;
    for (int j = i + 1; j < N; ++j) {
      if (!is_prime(j) && gcd(i, j) > 1) {
        b[j] = current_color;
      }
    }
    current_color += 1;
  }
  for (int i = 0; i < t; ++i) {
    scanf("%d\n", &n);
    m = 0;
    for (int j = 0; j < M; ++j) {
      c[j] = 0;
      d[j] = 0;
    }
    for (int j = 0; j < n; ++j) {
      scanf("%d", a + j);
      if (!c[b[a[j]]]) {
        c[b[a[j]]] += 1;
        m++;
      }
    }
    printf("%d\n", m);
    int current_color = 1;
    for (int j = 0; j < n; ++j) {
      if (d[b[a[j]]])
        printf("%d ", d[b[a[j]]]);
      else {
        d[b[a[j]]] = current_color;
        current_color++;
        printf("%d ", d[b[a[j]]]);
      }
    }
    printf("\n");
  }
}
