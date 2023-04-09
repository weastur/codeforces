#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 100500

int n, m, k, p;
char ans[N];

int main(int argc, const char *argv[]) {
  scanf("%d%d%d", &n, &m, &k);
  for (size_t i = 0; i < m - 1; i++) {
    ans[p++] = 'L';
  }
  for (size_t i = 0; i < n - 1; i++) {
    ans[p++] = 'D';
  }
  int i = 1;
  int j = 1;
  int cnt = n * m;
  while (cnt--) {
    if (i & 1) {
      if (j < m) {
        ans[p++] = 'R';
        j++;
      } else if (i != n) {
        ans[p++] = 'U';
        i++;
      }
    } else {
      if (j > 1) {
        ans[p++] = 'L';
        j--;
      } else if (i != n) {
        ans[p++] = 'U';
        i++;
      }
    }
  }

  printf("%d\n%s", strlen(ans), ans);
  return 0;
}
