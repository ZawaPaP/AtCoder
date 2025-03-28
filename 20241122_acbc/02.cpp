#include <bits/stdc++.h>
using namespace std;

int main() {

  string S;
  cin >> S;

  if ( S.size() % 2 != 0) {
      cout << "No" << endl;
      return 0;
  }
  int mid;
  mid = S.size() / 2;

  
  for (int i = 1; i <= mid; ++i) {
      int two_i_minus = 2 * i - 1;
      int two_i = 2 * i;

      if (S.at(two_i_minus - 1) != S.at(two_i - 1))
      {
          cout << "No" << endl;
          return 0;
      }
  }

  map<char, int> mp;

  for (int i = 0; i < S.size(); ++i) {
      mp[S.at(i)] += 1;
  }
  
  for (auto [key, value] : mp) {
      if (value != 2) {
        cout << "No" << endl;
          return 0;
      }
  }

  cout << "Yes" << endl;
}