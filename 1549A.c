#include <stdio.h>

int t, p;

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &p);
        printf("2 %d\n", p - 1);
    }
}
