#include <bits/stdc++.h>
using namespace std;


int main() {
    long long N, K;
    cin >> N >> K;
    vector<int> A(N + 1);
    vector<int> R(N + 1);

    for (int i = 1; i < N + 1; ++i)
    {
        cin >> A.at(i);
    }

    for (int i = 1; i < N + 1; ++i)
    {
        if (i == 1)
            R[i] = 1;
        else
            R[i] = R[i - 1];
        
        while (R[i] < N && A[R[i] + 1] - A[i] <= K)
        {
            R[i] += 1;
        }
    }
    long long Answer = 0;
	for (int i = 1; i <= N - 1; i++) Answer += (R[i] - i);
	cout << Answer << endl;
	return 0;
}

// 上は回答の写経。下が同じくスライディングウィンドウの別解

#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N, K;
    cin >> N >> K;
    vector<int> A(N + 1);

    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }

    long long total = 0;
    int j = 1;

    for (int i = 1; i <= N; ++i) {
        // jを進めていき、A[j] - A[i]がK以下になるように調整
        while (j <= N && A[j] - A[i] <= K) {
            j++;
        }
        
        // iからj-1までの部分列の数を加算
        total += (j - i - 1);
    }

    cout << total << endl;
    return 0;
}
