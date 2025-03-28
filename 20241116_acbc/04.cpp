#include <bits/stdc++.h>
using namespace std;




int main() {
    string S;
    cin >> S;

    string T;

    for (int i = 0; i < S.size(); ++i)
    {
        if ('a' <= S.at(i) && S.at(i) <= 'z') {
            T += char(S.at(i) - 'a' + 'A');
        }
        else {
            T += char(S.at(i) - 'A' + 'a');
        }
    }

    long long s = S.size();

    long long string_count = 0;
    long long char_count = 0;

    int Q;
    cin >> Q;

    for (int i = 0; i < Q; ++i) {
        long long k;
        cin >> k;

        char_count = k % s;

        bool reverse_flag = false;
        
        if (k > s) {
            if (string_count % 2 == 0) {
                string_count /= 2;
            }
            else {
                string_count = (string_count - 1) / 2 + 1;
             }
            reverse_flag = !reverse_flag;
        } else {
            string_count = 1;
        }

        // string countに対して、2のN番目かを考えるべきだった。

        while (string_count > 1)
        {
            if (string_count % 2 == 0) {
                string_count /= 2;
            }
            else {
                string_count = (string_count - 1) / 2 + 1;
             }

            reverse_flag = !reverse_flag;
            }
        if (reverse_flag) {
            if (char_count == 0) {
                cout << T.at(s - 1);
            } else {
                cout << T.at(char_count - 1);
            }
        } else {
            if (char_count == 0) {
                cout << S.at(s - 1);
            } else {
                cout << S.at(char_count - 1);
            }
        }
    if (i != Q - 1) {
        cout << " ";
    }
    }
    cout << endl;
}