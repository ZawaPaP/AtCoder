#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  string S;
  cin >> S;

  if ( n % 2 == 0) {
      cout << "No" << endl;
      return 0;
  }
  int mid;
  mid = n / 2;

  if (S.at(mid) != '/') {
      cout << "No" << endl;
      return 0;
  }

  for (int i = 0; i < mid; ++i) {
    if (S.at(i) != '1') {
        cout << "No" << endl;
        return 0;
    }
  }
  for (int i = mid + 1; i < n; ++i) {
        if (S.at(i) != '2') {
        cout << "No" << endl;
        return 0;
    }
  }
  cout << "Yes" << endl;
}