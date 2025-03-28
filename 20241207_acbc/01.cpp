#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<pair<int, int>> W(N + 1);

    for (int i = 1; i <= N; ++i) {
        int t, v;
        cin >> t >> v;
        W[i] = make_pair(t, v);
    }

    int prev_time = W[1].first;
    int water = W[1].second;
    for (int i = 2; i <= N; ++i)
    {
        water -= (W[i].first - prev_time);

        if (water < 0)
            water = 0;

        water += W[i].second;

        prev_time = W[i].first;
    }

    cout << water << endl;
}