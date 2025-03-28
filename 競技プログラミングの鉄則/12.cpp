#include <bits/stdc++.h>
using namespace std;

long long N, K;



bool check(long long x, vector<int>& A)
{
    long long print = 0;
    for (int i = 0; i < N; ++i)
    {
        print += x / A.at(i);
    }
    if (print >= K)
        return true;
    else
        return false;
}

int main() {
    cin >> N >> K;
    vector<int> A(N);

    for (int i = 0; i < N; ++i)
    {
        cin >> A.at(i);
    }

    long long l, r, mid;
    l = 1;
    r = 1000000000;

    while(l < r) {
        mid = (l + r) / 2;
        if (check(mid, A)) {
            r = mid;
        }
        else
            l = mid + 1;
    }
    cout << r << endl;
}
