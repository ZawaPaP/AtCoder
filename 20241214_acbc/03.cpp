#include <bits/stdc++.h>
using namespace std;

int main() {
    int a[5];
    for (int i = 0; i < 5; ++i) {
        cin >> a[i];
    }

    map<string, int> mp;
    string NAME = "ABCDE";

    for (int i = 0; i < (1 << 5); ++i) {
        bitset<5> bit(i);
        int sum = 0;
        for (int j = 0; j < 5; ++j) {
            if (bit[j]) {
                sum += a[j];
            }
        }
        string name;
        for (int j = 0; j < 5; ++j) {
            if (bit[j]) {
                name += NAME[j];
            }
        }
        mp[name] = sum;
    }


    vector<pair<int, string>> v;
    for (auto it = mp.begin(); it != mp.end(); ++it) {
        v.push_back(make_pair(it->second, it->first));
    }

    function<bool(pair<int, string>, pair<int, string>)> cmp = [](pair<int, string> a, pair<int, string> b) {
        if (a.first == b.first) {
            return a.second < b.second;
        }
        return a.first > b.first;
    };


    sort(v.begin(), v.end(), cmp);

    for (int i = 0; i < v.size(); ++i) {
        cout << v[i].second << endl;
    }

}