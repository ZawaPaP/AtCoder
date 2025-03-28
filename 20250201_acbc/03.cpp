#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;

    map<int, int> mp;
    vector<int> nestCount(N + 1, 0);
    int duplicateCount = 0;

    for (int i = 1; i <= N; i++) {
        mp[i] = i;
        nestCount[i] = 1;
    }
    // mapは 鳩: 存在する巣

    for (int i = 0; i < Q; i++) {
        int order;
        cin >> order;

        if (order == 1) {
            int P, H;
            cin >> P >> H;

            int prevNest = mp[P];
            nestCount[prevNest]--;
            if (nestCount[prevNest] == 1) {
                duplicateCount--;
            }
            mp[P] = H;
            nestCount[H]++;
            if (nestCount[H] == 2) {
                duplicateCount++;
            }
        }
        else {
            cout << duplicateCount << endl;
        }
    }
}