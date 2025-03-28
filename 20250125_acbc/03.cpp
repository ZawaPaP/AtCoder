#include <bits/stdc++.h>
using namespace std;

int main() {
    int H, W;
    cin >> H >> W;

    char A[H][W];
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            cin >> A[i][j];
        }
    }

    // 一番左の黒、一番右の黒、一番上の黒、一番下の黒を求める
    int left_black = W;
    int right_black = 0;
    int top_black = H;
    int bottom_black = 0;

    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (A[i][j] == '#') {
                left_black = min(left_black, j);
                right_black = max(right_black, j);
                top_black = min(top_black, i);
                bottom_black = max(bottom_black, i);
            }
        }
    }
    
    // 上記4つの中に、白が含まれていたらNG, 黒と?だけならOK
    for (int i = top_black; i <= bottom_black; ++i) {
        for (int j = left_black; j <= right_black; ++j) {
            if (A[i][j] == '.') {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    cout << "Yes" << endl;
    return 0;
}