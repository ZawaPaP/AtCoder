#include <bits/stdc++.h>
using namespace std;


int main() {
    int N,R;
    cin >> N >> R;

    long long answer = R;
    for (int i = 1; i <= N; ++i){
        int D, A;
        cin >> D >> A;
        if (D == 1 && (1600 <= answer && answer <= 2799)) {
            answer += A;
        }
        else if (D == 2 && (1200 <= answer && answer <= 2399)) {
            answer += A;
        }
    }

    cout << answer << endl;
}