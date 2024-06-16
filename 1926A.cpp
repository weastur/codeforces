// Problem: A. Влад и лучший из пяти
// Contest: Codeforces - Codeforces Round 928 (Div. 4)
// URL: https://codeforces.com/contest/1926/problem/A
// Memory Limit: 256 MB
// Time Limit: 1000 ms

#include <iostream>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    string s;
    cin >> s;
    int cnt = 0;
    for (int i = 0; i < s.size(); i++) {
      cnt += s[i] == 'A';
    }
    if (cnt > 2) {
      cout << "A\n";
    } else {
      cout << "B\n";
    }
  }
  return 0;
}
