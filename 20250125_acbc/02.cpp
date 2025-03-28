#include <bits/stdc++.h>
using namespace std;


int main() {
    int N;
    cin >> N;

    long double A[N];
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    if (N <= 2) {
        cout << "Yes" << endl;
        return 0;
    }

    // 公比が整数であることを確認する。
    if (A[1] > A[0]) {
        if (A[1] % A[0] != 0) {
            cout << "No" << endl;
            return 0;
        }
    }
    else {
        if (A[0] % A[1] != 0) {
            cout << "No" << endl;
            return 0;
        }
    }

    

    if (A[1] > A[0]) {
        long double multiplier = A[1] / A[0];
        for (int i = 1; i < N; ++i) {
            if (A[i] < A[i - 1]) {
            cout << "No" << endl;
            return 0;
            }
            if (A[i] % A[i - 1] != 0) {
            cout << "No" << endl;
            return 0;
            }   
            if (A[i] / A[i - 1] != multiplier) {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    else {
        long double multiplier = A[0] / A[1];
        for (int i = 1; i < N; ++i) {
            if (A[i] > A[i - 1]) {
            cout << "No" << endl;
            return 0;
            }
            if (A[i - 1] % A[i] != 0) {
                cout << "No" << endl;
                return 0;
            }
            if (A[i - 1] / A[i] != multiplier) {
                cout << "No" << endl;
                return 0;
            }
        }
    }

    cout << "Yes" << endl;
    return 0;
}