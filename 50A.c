#include <ctype.h>
#include <fenv.h>
#include <float.h>
#include <inttypes.h>
#include <limits.h>
#include <math.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) < (b)) ? (b) : (a))
#define ABS(x) (((x) <  0) ? -(x) : (x))
#define ODD(x) ((x) & 1)
#define EVEN(x) (!ODD((x)))
#define SWAP(a, b) do { a ^= b; b ^= a; a ^= b; } while(0)
#define ARRAY_SIZE(a) (sizeof(a) / sizeof(*a))
#ifdef LOCAL
#define LOG(x, fmt, ...) if(x){fprintf(stderr, "%s:%d: " fmt "\n",__FILE__, __LINE__, __VA_ARGS__);}
#else
#define LOG(x, fmt, ...) do { } while(0)
#endif

int main(void)
{
    int n, m;
    scanf("%d%d", &n, &m);
    printf("%d", (n*m)/2);
    return 0;
}

