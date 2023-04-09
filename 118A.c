#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
  const size_t MAXLEN = 102;
  char *s = malloc(MAXLEN * sizeof(char));
  char *p = malloc(MAXLEN * 2 * sizeof(char));
  fgets(s, MAXLEN, stdin);
  size_t len_s = strlen(s);
  size_t len_p = 0;
  for (size_t i = 0; i < len_s; i++) {
    if (!isalpha(s[i])) continue;
    char current_lower_char = tolower(s[i]);
    if (current_lower_char == 'a' || current_lower_char == 'o' ||
        current_lower_char == 'y' || current_lower_char == 'e' ||
        current_lower_char == 'u' || current_lower_char == 'i')
      continue;
    p[len_p++] = '.';
    p[len_p++] = current_lower_char;
  }
  p[len_p] = 0;
  puts(p);
  return 0;
}