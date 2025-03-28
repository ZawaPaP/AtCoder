#include <bits/stdc++.h>
using namespace std;

int N, M, A[100009], B[1000009];
vector<int> G[1000009];
int dist[1000009];


int main(){
    cin >> N >> M;
    for (int i = 1; i <= M; ++i) {
        cin >> A[i] >> B[i];
        G[A[i]].push_back(B[i]);
        G[B[i]].push_back(A[i]);
    }

    for (int i = 1; i <= N; ++i) {
        dist[i] = -1;
    }

    queue<int> Q;
    Q.push(1);
    dist[1] = 0;

    while (!Q.empty())
    {
        int pos = Q.front();
        Q.pop();

        for (int i = 0; i < (int)G[pos].size(); ++i){
            int nex = G[pos][i];

            if (dist[nex] == -1) {
                dist[nex] = dist[pos] += 1;
                Q.push(nex);
            }
        }
    }

    for (int i = 0; i <= N; ++i){
        cout << dist[i] << endl;
    }
}
