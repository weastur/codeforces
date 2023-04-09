#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 200500

int n, k;
char s[N];

int main() {
  scanf("%d%d\n", &n, &k);
  scanf("%s", s);
  if (n == 1 && ((s[1] != '0' && k) || s[1] == '0')) {
    printf("0");
    return 0;
  }
  for (int i = 0; i < n; i++) {
    if (!k) break;
    if (i == 0 && s[i] != '1') {
      s[i] = '1';
      k--;
    } else if (i > 0 && s[i] != '0') {
      s[i] = '0';
      k--;
    }
  }
  printf("%s", s);
  return 0;
}