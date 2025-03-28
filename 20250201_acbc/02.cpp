#include <bits/stdc++.h>
using namespace std;

bool check(vector<vector<char>> S, vector<vector<char>> T, int i, int j, int M) {
    for (int x = 0; x < M; x++) {
        for (int y = 0; y < M; y++) {
            if (S[i + x][j + y] != T[x][y]) {
                return false;
            }
        }
    }
    return true;
}

int main()
{
    int N, M;
    cin >> N >> M;

    vector<vector<char>> S(N, vector<char>(N));
    vector<vector<char>> T(M, vector<char>(M));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> S[i][j];
        }
    }

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            cin >> T[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (S[i][j] == T[0][0] && i + M <= N && j + M <= N) {
                if (check(S, T, i, j, M)) {
                    cout << i + 1 << " " << j + 1 << endl;
                    return 0;
                }
            }
        }
    }
}
