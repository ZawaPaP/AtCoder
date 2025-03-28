#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int N, K;
  cin >> N >> K;
  vector<int> A(N);
  for (auto& a : A) cin >> a;
  int M = *max_element(begin(A), end(A));
  
  vector<int> s(M + 1), t(M + 1), u(M + 1);
  
  // 出現回数をカウント
  for (auto& a : A) {
    s[a]++;
    cout << "数 " << a << " の出現回数: " << s[a] << endl;
  }
  
  // 倍数の出現回数を集計
  for (int d = 1; d <= M; d++) {
    for (int n = d; n <= M; n += d) {
      t[d] += s[n];
    }
    cout << d << " の倍数の出現回数合計: " << t[d] << endl;
  }
  
  // 条件を満たす約数の最大値を記録
  for (int d = 1; d <= M; d++) {
    if (t[d] < K) continue;
    for (int n = d; n <= M; n += d) {
      u[n] = max(u[n], d);
    }
    cout << d << " は条件を満たすので、その倍数を更新" << endl;
  }
  
  // 結果出力
  for (auto& a : A) cout << u[a] << "\n";
}
