#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, X;
    cin >> N >> X;

    vector<int> A(N + 1);

    for (int i = 1; i <= N; ++i)
    {
        cin >> A.at(i);
    }

    int l, r, mid;
    l = 1;
    r = N;

    while (l <= r) {
        mid = (l + r) / 2;
        if(A.at(mid) == X) {
            cout << mid << endl;
            break;
        }
        else if (A.at(mid) > X) {
            r = mid;
        }
        else {
            l = mid + 1;
        }
    }
}
