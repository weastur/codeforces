#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 200500
#define M 30

int t, n, k, cnt[M], cnt2[M];
char s[N];

int main(int argc, const char *argv[]) {
  scanf("%d", &t);
  while (t--) {
    scanf("%d%d\n", &n, &k);
    scanf("%s\n", &s);
    int ans = 0;
    // if ((n / k) % 2 == 0) {
    //     for (int i = 0; i < k; ++i) {
    //         int current_pos = i;
    //         memset(cnt, 0, M * sizeof(int));
    //         while (current_pos < n) {
    //             cnt[s[current_pos] - 'a']++;
    //             current_pos += k;
    //         }
    //         int mmax = 0;
    //         for (int j = 0; j < M; ++j) {
    //             if (cnt[j] > mmax) {
    //                 mmax = cnt[j];
    //             }
    //         }
    //         printf("~~~%d\n", n / k - mmax);
    //         ans += n / k - mmax;
    //     }
    // } else {
    for (int i = 0; i <= k / 2; ++i) {
      int current_pos = i;
      if (k % 2 == 0 && i == k / 2) break;
      memset(cnt, 0, M * sizeof(int));
      memset(cnt2, 0, M * sizeof(int));
      while (current_pos < n) {
        cnt[s[current_pos] - 'a']++;
        if (k % 2 != 0 && i == k / 2) {
          current_pos += k;
          continue;
        } else {
          cnt2[s[n - (current_pos / k) * k - i - 1] - 'a']++;
          current_pos += k;
        }
      }
      int mmax = 0;
      for (int j = 0; j < M; ++j) {
        if (cnt[j] + cnt2[j] > mmax) {
          mmax = cnt[j] + cnt2[j];
        }
      }
      int p = 2;
      if (k % 2 != 0 && i == k / 2) p = 1;
      ans += p * n / k - mmax;
    }
    printf("%d\n", ans);
  }
  return 0;
}