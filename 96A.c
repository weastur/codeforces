#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
  const size_t MAXLEN = 100;
  char *s = malloc((MAXLEN + 1) * sizeof(char));
  scanf("%s\n", s);
  size_t len = strlen(s);
  size_t current_eq = 1;
  for (size_t i = 1; i < len; i++) {
    if (s[i] == s[i - 1])
      current_eq++;
    else
      current_eq = 1;
    if (current_eq == 7) {
      puts("YES");
      return 0;
    }
  }
  puts("NO");
  return 0;
}