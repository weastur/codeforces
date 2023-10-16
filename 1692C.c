#include <stdio.h>
#include <string.h>

#define N 9

char d[N][N];
int t;

int main() {
    scanf("%d", &t);
    while (t--) {
        for (int i = 0; i < 8; i++)
            scanf("%s\n", d + i);
        for (int r = 1; r < 7; r++)
            for (int c = 1; c < 7; c++)
                if (d[r][c] == '#' && d[r - 1][c - 1] == '#' && d[r - 1][c + 1] == '#' && d[r + 1][c - 1] == '#' && d[r + 1][c + 1] == '#')
                    printf("%d %d\n", r + 1, c + 1);
    }
}
