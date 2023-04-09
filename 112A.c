#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
  const size_t MAXLEN = 100;

  char *s = malloc((MAXLEN + 1) * sizeof(char));
  char *t = malloc((MAXLEN + 1) * sizeof(char));

  scanf("%s\n", s);
  scanf("%s\n", t);

  size_t len = strlen(s);

  for (size_t i = 0; i < len; i++)
    if (tolower(s[i]) < tolower(t[i])) {
      puts("-1");
      return 0;
    } else if (tolower(s[i]) > tolower(t[i])) {
      puts("1");
      return 0;
    }
  puts("0");
  return 0;
}