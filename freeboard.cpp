#include <bits/stdc++.h>

using namespace std;


int main() {
    int N;
    long long X[100009], Y[100009];
    long long A, B;
    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> X[i] >> Y[i];
    }
    cin >> A >> B;

    int cnt = 0;
    for (int i = 0; i < N; ++i) {
        long long xa = X[i] - A;
        long long ya = Y[i] - B;
        long long xb = X[(i + 1) % N] - A;
        long long yb = Y[(i + 1) % N] - B;

        if (ya > yb) {
            swap(xa, xb);
            swap(ya, yb);
        }

        if (ya <= 0 && 0 < yb && xa * yb - ya * xb < 0) {
            cnt++;
        }
    }

    if (cnt % 2 == 1) {
        cout << "INSIDE" << endl;
    } else {
        cout << "OUTSIDE" << endl;
    }
}
