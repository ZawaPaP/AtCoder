#include <bits/stdc++.h>
using namespace std;


int main()
{
    int N, W;
    cin >> N >> W;

    // key: block number
    // value: 消える秒数
    // -1 の場合は消えない
    map<int, int> mp;

    // 各列のブロック個数
    vector<int> blockCount(W + 1, 0);

    // 各列のブロック高さ
    // tuple(y, block number)
    vector<vector<pair<int, int>>> blockHeight(W + 1, vector<pair<int, int>>());

    
    for (int i = 1; i <= N; i++) {
        int x, y;
        cin >> x >> y;
        blockCount[x]++;
        blockHeight[x].push_back(make_pair(y, i));
        mp[i] = -1;
    }

    // 各列ごとのブロック個数の最小値
    int minBlockCount = N;
    for (int i = 1; i <= W; i++) {
        minBlockCount = min(minBlockCount, blockCount[i]);
    }

    // 各列ごとのブロック高さでソート
    for (int i = 1; i <= W; i++) {
        sort(blockHeight[i].begin(), blockHeight[i].end());
    }


    vector<int> minBlockHeight(minBlockCount + 1, 0);
    for (int i = 0; i < minBlockCount; i++) {
        for (int j = 1; j <= W; j++) {
            minBlockHeight[i] = max(minBlockHeight[i], blockHeight[j][i].first);
        }
    }


    // minBlockCount * 列が消えるブロック数
    // 消える順番はblockHeightの順番
    // 下から数えたときに、(yが小さい時)ブロック最小値の範囲内にあるブロックは消える秒数を計算
    for (int i = 0; i < minBlockCount; i++) {
        for (int j = 1; j <= W; j++) {
            int blockNum = blockHeight[j][i].second;
            mp[blockNum] = minBlockHeight[i];
        }
    }

    int Q;
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        int T, A;
        cin >> T >> A;
        if (mp[A] == -1 || mp[A] > T) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
}