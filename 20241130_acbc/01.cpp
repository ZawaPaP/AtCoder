#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, D;
  cin >> N >> D;

  string S;
  cin >> S;

  int count = 0;
  for (int i = 0; i < N; ++i)
  {
      if (S.at(i) == '@')
      {
          count += 1;
      }
  }

  cout << S.size() - (count - D) << endl;
}