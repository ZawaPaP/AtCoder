#include <bits/stdc++.h>
using namespace std;

int N, M, A[100009], B[1000009];
vector<int> G[1000009];
bool visited[1000009];

void dfs(int pos) {
    visited[pos] = true;
    for (int i: G[pos]) {
        if (visited[pos] == false)
            dfs(pos);
    }
}

int main(){
    cin >> N >> M;
    for (int i = 1; i <= M; ++i){
        cin >> A[i] >> B[i];
        G[A[i]].push_back(B[i]);
        G[B[i]].push_back(A[i]);
    }

    dfs(1);

    bool Answer = true;
    for (int i = 1; i <= N; ++i){
        if (visited[i] == false)
            Answer = false;
    }

    if (Answer) {
        cout << "The graph is connected." << endl;
    } else {
        cout << "Rhe graph is not connected." << endl;
    }
}
