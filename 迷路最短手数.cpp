#include <bits/stdc++.h>
using namespace std;

int R, C, sx, sy, gx, gy;


int main(){
    cin >> R >> C >> sy >> sx >> gy >> gx;

    vector<string> L(R + 1);
    vector<vector<int>> dist(R + 1, vector<int>(C + 1, -1));

    for (int i = 1; i <= R; ++i){
        cin >> L[i];
        // 1 からのインデックスにするために、 # を追加
        L[i] = " " + L[i];
    }

    queue<pair<int, int>> Q;
    Q.push(make_pair(sy, sx));
    dist[sy][sx] = 0;

    while (!Q.empty())
    {
        pair<int, int> pos = Q.front();
        Q.pop();

        int dx[] = {0, 1, 0, -1};  // 右、下、左、上
        int dy[] = {1, 0, -1, 0};
        
        for (int dir = 0; dir < 4; ++dir) {
            int mx = pos.second + dx[dir];
            int my = pos.first + dy[dir];
                // 周囲は壁
            if (1 <= mx && mx <= C && 1 <= my && my <= R) {
                if (L[my][mx] != '#' && dist[my][mx] == -1)
                {
                    dist[my][mx] = dist[pos.first][pos.second] + 1;
                    Q.push(make_pair(my, mx));
                }
            }
        }
    }
    cout << dist[gy][gx] << endl;
}
