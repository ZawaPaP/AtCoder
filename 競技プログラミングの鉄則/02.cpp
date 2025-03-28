#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, X;
    cin >> N >> X;

    set<int> S;

    for (int i = 0; i < N; ++i) {
        int a;
        cin >> a;
        S.insert(a);
    }
    if (S.count(X)) {
        cout << "Yes" << endl;
        return 0;
    }
    cout << "No" << endl;
}
