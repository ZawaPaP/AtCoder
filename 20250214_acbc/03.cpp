#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    int selfLoopCount = 0;
    int multiEdgeCount = 0;

    set<pair<int, int>> lineSet;

    vector<vector<int>> A(N + 1, vector<int>(0));
    for (int i = 1; i <= M; i++) {
        int a,b;
        cin >> a >> b;
        if (a == b) {
            selfLoopCount++;
            continue;
        }
        if (lineSet.count(make_pair(a, b))) {
            multiEdgeCount++;
            continue;
        }
        lineSet.insert(make_pair(a, b));
        lineSet.insert(make_pair(b, a));
        A[a].push_back(b);
    }
    cout << selfLoopCount + multiEdgeCount << endl;
}