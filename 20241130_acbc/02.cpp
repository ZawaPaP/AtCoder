#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, D;
  cin >> N >> D;

  string S;
  cin >> S;

  vector<char> vec(N);

  int count = 0;
  for (int i = 0; i < N; ++i)
  {
      vec[i] = S.at(i);
  }

  for (int i = 0; i < D; ++i) {
      for (int j = N - 1; j >= 0; --j)
      {
          if (vec[j] == '@')
          {
              vec[j] = '.';
              break;
          }
      }
  }
  for (int i = 0; i < N; ++i) {
      cout << vec[i];
  }
}