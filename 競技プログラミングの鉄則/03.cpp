#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;

    vector<int> p(N);
    vector<int> q(N);

    for (int i = 0; i < N; ++i) {
        cin >> p.at(i);
    }

        for (int i = 0; i < N; ++i) {
        cin >> q.at(i);
    }

    for (int i = 0; i < N; ++i) {
        if (count(q.begin(), q.end(), K - p.at(i))) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
}
