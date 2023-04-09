#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 1010

int n, ans, a[N], b[N];
char used[N];

int main(int argc, char *argv[]) {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) scanf("%d", a + i);
  for (int i = 0; i < n; i++) {
    int k = -1;
    for (int j = 0; j < n; j++) {
      if (!used[j] && (k == -1 || a[k] < a[j])) k = j;
    }
    used[k] = 1;
    b[i] = k + 1;
    ans += a[k] * i + 1;
  }
  printf("%d\n", ans);
  for (int i = 0; i < n; i++) printf("%d ", b[i]);

  return 0;
}