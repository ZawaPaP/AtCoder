#include <bits/stdc++.h>
using namespace std;

int main()
{
    string S;
    cin >> S;

    int ans = 0;
    int aIndex = -1;
    int bIndex = -1;
    int cIndex = -1;
    for (int i = 0; i < S.size(); i++) {
        if (S[i] != 'A') {
            continue;
        }else {
            aIndex = i;
        }

        for (int j = i + 1; j < S.size(); j++) {
            if (S[j] != 'B') {
                continue;
            }else {
                bIndex = j;
            }
            for (int k = bIndex + 1; k < S.size(); k++) {
                if (S[k] != 'C') {
                    continue;
                }else {
                    cIndex = k;
                }
                if (aIndex != -1 && bIndex != -1 && cIndex != -1) {
                    if (cIndex - bIndex == bIndex - aIndex) {
                        ans++;
                    }
                }
            }
        }
    }
    cout << ans << endl;
}
