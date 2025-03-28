#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;

    int count = 0;
    for (int i = 0; i < s.size(); ++i)
    {
        if (s.at(i) == '|')
        {
            if (count != 0) {
                cout << count;
                if (i != s.size() - 1) {
                    cout << " ";
                }
            }
            count = 0;
        }
        else {
            count++;
        }
    }
    cout << endl;

    return 0;
}