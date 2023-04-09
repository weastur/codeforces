#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int x1, x2, x3, x4, x5, x6, y1, y2, y3, y4, y5, y6;

void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

char inside(int x, int y, int x1, int y1, int x2, int y2) {
  if (x >= x1 && x <= x2 && y >= y1 && y <= y2) return 1;
  return 0;
}

int main() {
  scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
  scanf("%d%d%d%d", &x3, &y3, &x4, &y4);
  scanf("%d%d%d%d", &x5, &y5, &x6, &y6);

  if (!(inside(x1, y1, x3, y3, x4, y4) || inside(x1, y1, x5, y5, x6, y6))) {
    printf("YES");
    return 0;
  }
  if (!(inside(x2, y2, x3, y3, x4, y4) || inside(x2, y2, x5, y5, x6, y6))) {
    printf("YES");
    return 0;
  }
  if (!(inside(x1, y2, x3, y3, x4, y4) || inside(x1, y2, x5, y5, x6, y6))) {
    printf("YES");
    return 0;
  }
  if (!(inside(x2, y1, x3, y3, x4, y4) || inside(x2, y1, x5, y5, x6, y6))) {
    printf("YES");
    return 0;
  }

  if (inside(x1, y1, x3, y3, x4, y4) && inside(x2, y1, x3, y3, x4, y4) &&
      inside(x1, y2, x3, y3, x4, y4) && inside(x2, y2, x3, y3, x4, y4)) {
    printf("NO");
    return 0;
  }

  if (inside(x1, y1, x5, y5, x6, y6) && inside(x2, y1, x5, y5, x6, y6) &&
      inside(x1, y2, x5, y5, x6, y6) && inside(x2, y2, x5, y5, x6, y6)) {
    printf("NO");
    return 0;
  }

  if (x5 < x3) {
    swap(&x3, &x5);
    swap(&x4, &x6);
    swap(&y3, &y5);
    swap(&y4, &y6);
  }
  if (x4 + 1 <= x5 && x4 + 1 >= x1 && x4 + 1 <= x2) {
    printf("YES");
    return 0;
  }

  if (y6 > y4) {
    swap(&x3, &x5);
    swap(&x4, &x6);
    swap(&y3, &y5);
    swap(&y4, &y6);
  }
  if (y3 - 1 >= y6 && y3 - 1 <= y2 && y3 - 1 >= y1) {
    printf("YES");
    return 0;
  }

  printf("NO");

  return 0;
}