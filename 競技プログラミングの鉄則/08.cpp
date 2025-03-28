#include <bits/stdc++.h>
using namespace std;

int main() {
    int H, W;
    cin >> H >> W;

    vector<vector<int>> X(H + 1, vector<int>(W + 1, 0));
    
    // 横の累積和をとる
    for (int i = 1; i <= H; ++i) {
        for (int j = 1; j <= W; ++j) {
            int temp;
            cin >> temp;
            X[i][j] = temp + X[i][j - 1];
        }
    }

    int Q;
    cin >> Q;

    for (int i = 0; i < Q; ++i) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        int res = 0;
        for (int j = a; j <= c; ++j)
        {
            res += X[j][d] - X[j][b - 1];
        }
        cout << res << endl;
    }
}
