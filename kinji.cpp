#include <bits/stdc++.h>
using namespace std;


int main(){
    double r = 2.0;
    double a = 2.0;

    for (int i = 1; i <= 5; ++i) {
        double zahyou_x = a;
        double zahyou_y = a * a * a;

        //接線の式を求める y = (sessen_a) x + sessen_b とする。
        double sessen_a = 3.0 * zahyou_x* zahyou_x;
        double sessen_b = zahyou_y - sessen_a * zahyou_x;

        // y = 2 と 接線の交点のx座標が次のa
        double next_a = (r - sessen_b) / sessen_a;
        cout << setprecision(12) << next_a << endl;
        a = next_a;
    }
}
