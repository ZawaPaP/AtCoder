#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, K;
  cin >> N >> K;

  string S;
  cin >> S;

  int count;
  string between, move, res;
  char prev;
  prev = 0;
  count = 0;
  between = "";
  move = "";
  res = S.at(0);
  prev = S.at(0);

  bool flag = false;

  if (prev == '1') {
      count += 1;
  }

  for (int i = 1; i < N; ++i)
  {
    if (prev != S.at(i) && S.at(i) == '1') {
        count += 1;
    }
    prev = S.at(i);

    if (S.at(i) == '0' && count == K - 1) {
        between += S.at(i);
    } else if(S.at(i) == '1' && count == K) {
        move += S.at(i);
    } else if(S.at(i) == '0' && count == K && flag == false) {
        res += move;
        res += between;
        res += S.at(i);
        flag = true;
    } else {
        res += S.at(i);
    }
  }

  if (flag == false) {
      res += move;
      res += between;
    }

    cout << res << endl;
    return 0;
  }