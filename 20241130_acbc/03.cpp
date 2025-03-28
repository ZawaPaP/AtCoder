#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> A(N + 1);
    vector<int> B(M);
    vector<int> sorted_B(M);
    queue<int> que;

    for (int i = 1; i <= N; ++i)
    {
        cin >> A[i];
    }

    for (int i = 0; i < M; ++i)
    {
        int temp;
        cin >> temp;
        B[i] = temp;
        sorted_B[i] = temp;
    }

    sort(sorted_B.begin(), sorted_B.end(), greater<int>());

    map<int, int> mp;

    int cnt = 0;
    for (int i = 1; i <= N; ++i)
    {
        while (cnt < M && A[i] <= sorted_B[cnt]) {
            if (mp.count(sorted_B[cnt])) {
                cnt++;
                continue;
            }
            else{
                mp[sorted_B[cnt]] = i;
            }
            cnt++;
        }
    }

    for (int i = 0; i < M; ++i) {
        if (mp[B[i]])
            cout << mp[B[i]] << endl;
        else
            cout << -1 << endl;
    }
}