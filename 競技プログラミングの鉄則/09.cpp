#include <bits/stdc++.h>
using namespace std;

int main() {
    int H, W, N;
    cin >> H >> W >> N;

    // 横軸の累積話
    vector<map<int, int>> vec(H + 1);

    for (int i = 0; i < N; ++i) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        for (int j = a; j <= c; ++j)
        {
            vec[j][b] += 1;
            vec[j][d + 1] -= 1;
        }
    }

    for (int i = 1; i <= H; ++i) {
        int res;
        res = 0;
        for (int j = 1; j <= W; ++j)
        {
            res += vec[i][j];
            cout << res;
            if (j != W) {
                cout << " ";
            }
        }
        cout << endl;
    }
}
