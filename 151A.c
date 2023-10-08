#include <stdio.h>

int min3(int a, int b, int c) {
    int d = a < b ? a : b;
    return d < c ? d : c;
}

int main() {
    int n, k, l, c, d, p, nl, np;
    scanf("%d%d%d%d%d%d%d%d", &n, &k, &l, &c, &d, &p, &nl, &np);
    printf("%d\n", min3((k * l) / nl, c * d, p / np) / n);
}
