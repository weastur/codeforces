#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int a, b, c, d;

int main() {
  scanf("%d%d%d%d", &a, &b, &c, &d);
  if (a + b == c + d || a + c == b + d || a + d == b + c || b + c == a + d ||
      b + d == a + c || a + b + c == d || a + b + d == c || b + c + d == a ||
      b == a + c + d)
    printf("YES");
  else
    printf("NO");
  return 0;
}