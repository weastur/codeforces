#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
  const int MAXLEN = 102;
  int n = 0;
  scanf("%d\n", &n);
  char *s = malloc(MAXLEN * sizeof(char));
  while (n--) {
    fgets(s, MAXLEN, stdin);
    int len = strlen(s);
    if (len - 1 > 10) {
      printf("%c%d%c\n", s[0], len - 3, s[len - 2]);
    } else {
      printf(s);
    }
  }
  return 0;
}