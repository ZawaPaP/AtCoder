#include <bits/stdc++.h>
using namespace std;

int main() {
    int D, N;
    cin >> D >> N;

    vector<int> A(D + 1);

    A.at(0) = 0;

    // "X"日目の参加、帰宅人数をそれぞれ取得
    map<int, int> L;
    map<int, int> R;

    // 累積和
    for (int i = 0; i < N; ++i) {
        int l, r;
        cin >> l >> r;
        L[l] += 1;
        R[r] += 1;
    }

    for (int i = 1; i <= D; ++i) {
        A.at(i) = A.at(i - 1) + L[i] - R[i - 1];
        cout << A.at(i) << endl;
    }
}
