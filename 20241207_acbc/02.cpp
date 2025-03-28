#include <bits/stdc++.h>
using namespace std;


int main() {
    int H, W, D;
    cin >> H >> W >> D;

    vector<vector<char>> S(H + 1, vector<char>(W + 1));

    for (int i = 1; i <= H; ++i)
    {
        for (int j = 1; j <= W; ++j) {
            cin >> S[i][j];
        }
    }

    int total = 0;
    // 各床のマスについて、マンハッタン距離D以下のマス目数を数える
    for (int i1 = 1; i1 <= H; ++i1)
    {
        for (int j1 = 1; j1 <= W; ++j1) {
            if (S[i1][j1] == '#')
                continue;

            vector<vector<bool>> visited(H + 1, vector<bool>(W + 1, false));
            // S[i][j] に１台置いたとする
            int count1 = 0;
            for (int x = -D; x <= D; ++x) {
                for (int y = -D; y <= D; ++y) {
                    if (abs(x) + abs(y) > D)
                        continue;

                    int ni = i1 + x, nj = j1 + y;
                    if(ni < 1 || ni > H || nj < 1 || nj > W)
                        continue;
                    if (S[ni][nj] == '.' && !visited[ni][nj]) {
                        visited[ni][nj] = true;
                        count1++;
                    }
                }
            }
            for (int i2 = 1; i2 <= H; ++i2)
            {
                for (int j2 = 1; j2 <= W; ++j2) {
                    if (S[i2][j2] == '#')
                        continue;

                    vector<vector<bool>> temp_visited = visited;
                    int count2 = count1;

                    for (int x = -D; x <= D; ++x) {
                        for (int y = -D; y <= D; ++y) {
                            if (abs(x) + abs(y) > D)
                                continue;

                            int ni = i2 + x, nj = j2 + y;
                            if(ni < 1 || ni > H || nj < 1 || nj > W)
                                continue;
                            if (S[ni][nj] == '.' && !temp_visited[ni][nj]) {
                                temp_visited[ni][nj] = true;
                                count2++;
                            }
                        }
                    }
                total = max(total, count2);
                }
            }
        }
    }
    cout << total << endl;
}