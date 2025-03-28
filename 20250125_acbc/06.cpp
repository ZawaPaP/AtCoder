#include <bits/stdc++.h>
using namespace std;


int f(int x) {
    if (x % 2 != 0) {
        return x;
    }
    return f(x / 2);
}

int main()
{
    int N;
    cin >> N;

    vector<int> A(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }

    long long ans = 0;
    for (int i = 1; i <= N; ++i)
    {
        for (int j = i; j <= N; ++j) {
            ans += f(A[i] + A[j]);
        }
    }
    cout << ans << endl;
}
