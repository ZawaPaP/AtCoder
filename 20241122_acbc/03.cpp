#include <bits/stdc++.h>
using namespace std;

int N;
string S;

int check_length(int i) {
    int l_pointer = i - 1;
    int r_pointer = i + 1;

    while (l_pointer >= 0 && r_pointer < N) {
        if (S.at(l_pointer) != '1' || S.at(r_pointer) != '2') {
            break;
        };
        l_pointer -= 1;
        r_pointer += 1;
    }

    return r_pointer - l_pointer -  1;
}

int main() {
    cin >> N;
    cin >> S;

    int res = 0;
    for (int i = 0; i < N; ++i)
    {
        if (S.at(i) != '/') 
            continue;
        else
            res = max(check_length(i), res);
    }

    cout << res << endl;
}