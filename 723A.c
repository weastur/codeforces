#include <stdio.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int x, y, z, max, min;

int main() {
    scanf("%d%d%d", &x, &y, &z);
    printf("%d\n", MAX(MAX(x, y), z) - MIN(MIN(x, y), z));
}
