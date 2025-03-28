#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;

    vector<vector<char>> S(N + 1, vector<char>(N + 1));

    for (int i = 1; i < N + 1; i++) {
        int j = N + 1 - i;
        if (i > j) {
            continue;
        }

        for (int k = i; k <= j; k++) {
            for (int l = i; l <= j; l++) {
                if (i % 2 == 0) {
                    S[k][l] = '.';
                } else {
                    S[k][l] = '#';
                }
            }
        }
    }

    for (int i = 1; i < N + 1; i++) {
        for (int j = 1; j < N + 1; j++) {
            cout << S[i][j];
        }
        cout << endl;
    }
}
