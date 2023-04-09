#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 100500

int t, n, k, g, non_married;
char flag, used[N];

int main(int argc, const char* argv[]) {
  scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);
    memset(used, 0, n);
    non_married = -1;
    for (size_t i = 0; i < n; ++i) {
      flag = 0;
      scanf("%d", &k);
      for (size_t j = 0; j < k; ++j) {
        scanf("%d", &g);
        if (!used[g - 1] && !flag) {
          used[g - 1] = 1;
          flag = 1;
        }
      }
      if (!flag) {
        non_married = i;
      }
    }
    if (non_married == -1) {
      printf("OPTIMAL\n");
    } else {
      printf("IMPROVE\n");
      int ans = -1;
      for (size_t j = 0; j < n; ++j) {
        if (!used[j]) {
          ans = j;
        }
      }
      printf("%d %d\n", non_married + 1, ans + 1);
    }
  }
  return 0;
}
