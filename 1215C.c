#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 200500
int n, x, y;
char s[N], t[N];

int main(int argc, char *argv[]) {
  scanf("%d", &n);
  scanf("%s", s);
  scanf("%s", t);
  for (int i = 0; i < n; i++) {
    if (s[i] == t[i]) {
      continue;
    }
    if (s[i] == 'a' && t[i] == 'b') {
      x++;
    } else if (s[i] == 'b' && t[i] == 'a') {
      y++;
    }
  }
  if ((x + y) % 2) {
    printf("-1");
    return 0;
  } else {
    char odd = x % 2;
    char printed = !odd;
    if (odd) {
      printf("%d\n", x / 2 + y / 2 + 2);
    } else {
      printf("%d\n", x / 2 + y / 2);
    }
    int j = n;
    for (int i = 0; i < n; i++) {
      if (s[i] == 'a' && t[i] == 'b') {
        if (!printed) {
          printf("%d %d\n", i + 1, i + 1);
          printed = 1;
          t[i] = 'a';
          s[i] = 'b';
          continue;
        }
        while (1) {
          j--;
          if (s[j] == 'a' && t[j] == 'b') {
            printf("%d %d\n", i + 1, j + 1);
            t[i] = 'a';
            s[j] = 'b';
            break;
          }
        }
      }
    }
    j = n;
    for (int i = 0; i < n; i++) {
      if (s[i] == 'b' && t[i] == 'a') {
        while (1) {
          j--;
          if (s[j] == 'b' && t[j] == 'a') {
            printf("%d %d\n", i + 1, j + 1);
            t[i] = 'b';
            s[j] = 'a';
            break;
          }
        }
      }
    }
  }

  return 0;
}