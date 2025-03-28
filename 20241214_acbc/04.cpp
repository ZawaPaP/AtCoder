#include <bits/stdc++.h>
using namespace std;

    int main()
{
    int N;
    long long S;
    cin >> N >> S;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    long long sum = 0;
    for (int i = 0; i < N; ++i) {
        sum += A[i];
    }

    if (S % sum == 0) {
        cout << "Yes" << endl;
        return 0;
    }

    long long amari = S % sum;

    int l = 0;
    int r = 0;
    long long window_sum = A[0];
    while (l < N) {
        if (window_sum == amari) {
            cout << "Yes" << endl;
            return 0;
        }
        else if (window_sum > amari) {
            window_sum -= A[l];
            l++;
        }
        else if (window_sum < amari) {
            if (r < N - 1) {
                r++;
                window_sum += A[r];
            }
            else {
                r = 0;
                window_sum += A[r];
            }
        }
    }

    cout << "No" << endl;

}