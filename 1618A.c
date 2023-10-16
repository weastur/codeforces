#include <stdio.h>

#define N 7

int t, b[N], c;

int main() {
    scanf("%d", &t);
    while (t--) {
        for (int i = 0; i < 7; i++)
            scanf("%d", b + i);
        if (b[0] + b[1] == b[2])
            c = b[3];
        else
            c = b[2];
        printf("%d %d %d\n", b[0], b[1], c);
    }
}
