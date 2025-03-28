#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    // 横軸の累積話
    vector<int> A(N);

    for (int i = 0; i < N; ++i) {
        cin >> A.at(i);
    }

    //左から見る、部屋の最大人数
    vector<int> L(N + 2, 0);
    //右から見る、部屋の最大人数
    vector<int> R(N + 2, 0);

    int l_max, r_max;
    l_max = 0;
    r_max = 0;
    for (int i = 1; i <= N; ++i)
    {
        l_max = max(l_max, A.at(i - 1));
        L.at(i) = l_max;
        r_max = max(r_max, A.at(N - i));
        R.at(N - i + 1) = r_max;
    }
    // 例：
    // 1 2 5 5 2 3 1
    // L: 0 1 2 5 5 5 5 5 0
    // R: 0 5 5 5 5 3 3 1 0

    int D;
    cin >> D;

    for (int i = 0; i < D; ++i) {
        int l, r;
        cin >> l >> r;
        cout << max(L.at(l - 1), R.at(r + 1)) << endl;
    }
}
