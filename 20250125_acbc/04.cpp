#include <bits/stdc++.h>
using namespace std;


    long long calc_xor_pattern(vector<long long> a) {
        long long xor_pattern = 0;
        for (size_t i = 0; i < a.size(); ++i) {
            xor_pattern ^= a[i];
        }
        return xor_pattern;
    }




    int main()
{
    int N;
    cin >> N;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    set<long long> xor_patterns;

    // 任意の2つの袋の石をmergeすることを、任意回数できるとしたときに、袋の石の個数のパターンを求める。
    // 操作方法は操作回数を i として (n-i)C2 通りある
    // これは、0個の袋を選んでも結果がかわらず、操作をするたびに医師が0個の袋が増えていくため。
    // 操作回数の最大は、N-1回。

    queue<vector<long long>> q;
    set<vector<long long>> stones;

    sort(A.begin(), A.end());
    q.push(A);
    while (!q.empty()) {
        vector<long long> a = q.front();
        q.pop();

        if (stones.count(a)) 
            continue;
        stones.insert(a);

        int xor_pattern = calc_xor_pattern(a);
        xor_patterns.insert(xor_pattern);


        for (size_t i = 0; i < a.size(); ++i) {
            for (size_t j = i+1; j < a.size(); ++j) {
                if (a[i] == 0 || a[j] == 0) continue;
                vector<long long> a_tmp = a;
                a_tmp[i] += a_tmp[j];
                a_tmp[j] = 0;
                sort(a_tmp.begin(), a_tmp.end());
                q.push(a_tmp);
            }
        }
    }

    cout << xor_patterns.size() << endl;
    return 0;
}