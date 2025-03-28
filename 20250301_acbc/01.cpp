#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    bool ans = true;
    for (int i = 1; i < N; i++) {
        if (A[i] - A[i - 1] <= 0) {
            ans = false;
        }
    }
    cout << (ans ? "Yes" : "No") << endl;
}