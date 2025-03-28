#include <bits/stdc++.h>
using namespace std;

int main() {
    int a[5];
    for (int i = 0; i < 5; ++i) {
        cin >> a[i];
    }

    bool flag = false;

    for (int i = 1; i < 5; ++i) {
        if (a[i] < a[i - 1] && !flag) {
            swap(a[i], a[i - 1]);
            flag = true;
        }
    }

    if (!flag) {
        cout << "No" << endl;
        return 0;
    }

    for (int i = 1; i < 5; ++i)
        {
            if (a[i] < a[i - 1]) {
                cout << "No" << endl;
                return 0;
            }
        }

    cout << "Yes" << endl;
    return 0;
}