#include <bits/stdc++.h>
using namespace std;

int N, M, A[100009], B[1000009];
vector<int> G[1000009];
bool visited[1000009];

int main(){
    cin >> N >> M;
    for (int i = 1; i <= M; ++i){
        cin >> A[i] >> B[i];
        G[A[i]].push_back(B[i]);
        G[B[i]].push_back(A[i]);
    }

    for (int i = 1; i <= N; ++i){
        visited[i] = false;
    }

    stack<int> S;
    visited[1] = true;
    S.push(1);

    while (!S.empty())
    {
        int pos = S.top();
        S.pop();
        for (int nex: G[pos]) {
            if(visited[nex] == false) {
                visited[nex] = true;
                S.push(nex);
            }
        }
    }

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
