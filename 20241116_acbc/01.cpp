#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

    vector<int> a(n);

    a[1] = n / 100000;
    n %= 100000;
    a[2] = n / 10000;
    n %= 10000;
    a[3] = n / 1000;
    n %= 1000;
    a[4] = n / 100;
    n %= 100;   
    a[5] = n / 10;
    n %= 10;
    a[6] = n / 1;

    if (count(a.begin(), a.end(), 1) == 1 && count(a.begin(), a.end(), 2) == 2 && count(a.begin(), a.end(),3)==3){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}