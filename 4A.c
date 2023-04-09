#include <stdio.h>

int main(int argc, char *argv[]) {
  int w;
  scanf("%d", &w);
  if (w & 1 || w == 2) {
    printf("NO");
  } else {
    printf("YES");
  }
  return 0;
}