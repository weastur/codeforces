// Problem: A. Квадрат
// Contest: Codeforces - Codeforces Round 920 (Div. 3)
// URL: https://codeforces.com/contest/1921/problem/A
// Memory Limit: 256 MB
// Time Limit: 1000 ms

#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    vector<int> x(4), y(4);
    cin >> x[0] >> y[0] >> x[1] >> y[1] >> x[2] >> y[2] >> x[3] >> y[3];
    sort(x.begin(), x.end());
    sort(y.begin(), y.end());
    cout << (x[3] - x[0]) * (y[3] - y[0]) << '\n';
  }
  return 0;
}
