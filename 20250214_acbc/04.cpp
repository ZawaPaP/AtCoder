#include <bits/stdc++.h>
using namespace std;

vector<long long> oneIndex;
vector<long long> diffs;
long long totalDiff = 0;

int main()
{
    int N;
    string S;
    cin >> N >> S;

    int oneCount = 0;
    // 1のindexを集める
    for (long long i = 0; i < N; i++) {
        if (S[i] == '1') {
            oneIndex.push_back(i);
            oneCount++;
        }
    }

    if (oneCount == 1) {
        cout << 0 << endl;
        return 0;
    }

    // oneIndexの差
    
    for (long long i = 0; i < oneIndex.size() - 1; i++) {
        long long diff = oneIndex[i + 1] - oneIndex[i] - 1;
        totalDiff += diff;
        diffs.push_back(diff);
    }

    // 初期値は全て左端の１に合わせるとして
    long long work = 0;
    for (long long i = 0; i < diffs.size(); i++) {
        work += diffs[i] * (oneIndex.size() - (i + 1));
    }

    vector<long long> works;
    works.push_back(work);
    long long minWork = work;
    for (long long i = 1; i < oneIndex.size(); i++) {
        long long newWork = works[i - 1]  - (diffs[i - 1] * (oneIndex.size() - i)) + (diffs[i - 1] * i);
        works.push_back(newWork);
        minWork = min(minWork, newWork);
    }

    cout << minWork << endl;
    

}