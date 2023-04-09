#include <stdio.h>

int l, r;
char used[10];

int main() {
  scanf("%d%d", &l, &r);
  for (int i = l; i <= r; ++i) {
    for (int j = 0; j < 10; j++) used[j] = 0;
    int ans = i;
    char found = 1;
    while (ans) {
      int c = ans % 10;
      used[c]++;
      if (used[c] > 1) {
        found = 0;
        break;
      }
      ans = ans / 10;
    }
    if (found) {
      printf("%d", i);
      return 0;
    }
  }
  printf("-1");
  return 0;
}