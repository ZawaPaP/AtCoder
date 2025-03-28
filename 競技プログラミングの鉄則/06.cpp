#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;

    vector<int> A(N + 1);

    A.at(0) = 0;
    // 累積和
    for (int i = 1; i <= N; ++i) {
        int temp;
        cin >> temp;
        A.at(i) = A.at(i - 1) + temp;
    }

    for (int i = 0; i < Q; ++i) {
        int first, end;
        cin >> first >> end;
        cout << A.at(end) - A.at(first) << endl;
    }
}
