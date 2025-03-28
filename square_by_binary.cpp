#include <bits/stdc++.h>
using namespace std;


int main(){
    double l = 1.0;
    double r = 2.0;


    for (int i = 1; i <= 15; ++i){
        double mid = (l + r) / 2;
        if (mid * mid < 2.0)
            l = mid;
        else
            r = mid;

        cout << setprecision(7) << mid << endl;
    }
}
