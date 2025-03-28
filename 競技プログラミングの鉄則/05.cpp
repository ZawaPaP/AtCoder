#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;

    int res = 0;

    for (int i = 1; i <= N; ++i)
    {
        for (int j = 1; j <= min(K - i, N); ++j) {
            if ((K - i - j) > 0 && (K - i - j) <= N){
                res += 1;
            }
        }
    }
    cout << res << endl;
}
