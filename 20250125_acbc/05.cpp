#include <bits/stdc++.h>
using namespace std;

    int main()
{
    int H, W, X;
    cin >> H >> W >> X;
    int P, Q;
    cin >> P >> Q;

    vector<vector<long long>> S(H + 1, vector<long long>(W + 1));
    for (int i = 1; i <= H; ++i) {
        for (int j = 1; j <= W; ++j) {
            cin >> S[i][j];
        }
    }

    vector<vector<bool>> takahashi_area(H + 1, vector<bool>(W + 1, false));
    takahashi_area[P][Q] = true;

    vector<pair<int, int>> takahashi_area_list;
    takahashi_area_list.push_back(make_pair(P, Q));

    long long strong_point = S[P][Q];

    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};

    bool flag = true;

    while(flag) {
        flag = false;
        for (int i = 0; i < takahashi_area_list.size(); ++i) {
            int x = takahashi_area_list[i].first;
            int y = takahashi_area_list[i].second;
            for (int j = 0; j < 4; ++j) {
                int nx = x + dx[j];
                int ny = y + dy[j];
                if (nx < 1 || nx > H || ny < 1 || ny > W) {
                    continue;
                }
                if (takahashi_area[nx][ny]) {
                    continue;
                }
                if (S[nx][ny] < (strong_point + X - 1) / X) {
                    strong_point += S[nx][ny];
                    takahashi_area[nx][ny] = true;
                    takahashi_area_list.push_back(make_pair(nx, ny));
                    flag = true;
                }
            }
        }
    }

    cout << strong_point << endl;
}