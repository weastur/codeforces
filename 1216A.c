#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 200500

int n, ans;
char s[N], t[N];

int main(int argc, char *argv[]) {
  scanf("%d\n%s", &n, s);
  for (int i = 0; i < n; i++) {
    if ((i + 1) % 2) {
      t[i] = s[i];
      continue;
    }
    if (s[i] == s[i - 1]) {
      ans++;
      if (s[i] == 'a')
        t[i] = 'b';
      else
        t[i] = 'a';
    } else {
      t[i] = s[i];
    }
  }
  printf("%d\n%s\n", ans, t);
  return 0;
}