#include <bits/stdc++.h>
using namespace std;

bool mp_check(map<int, int>& mp) {
    for (auto [key, value] : mp) {
      if (value != 2) {
        return false;
      }
  }
  return true;
}


int main() {
    int N;
    cin >> N;
    vector<int> A(N);

    for (int i = 0; i < N; ++i)
    {
        cin >> A[i];
    }

    if (N  == 1) {
        cout << 0 << endl;
        return 0;
    }

    // Nが2以上とする

    map<int, int> mp;

    int left_pointer = 0;
    int right_pointer = 1;
    int left_length = 1;
    int right_length = 0;
    int res_length = 0;

    int temp = -1;
    mp[A[0]] = 1;
    while (right_pointer < N)
    {
        if (A[left_pointer] == A[right_pointer] && mp[A[right_pointer]] < 2) {
            mp[A[right_pointer]] += 1;
        }
        else {
            // 異なる数字に当たった場合、ここまでの数値が全部偶数だったら継続
            if (mp_check(mp) && mp[A[right_pointer]] < 2) {
                mp[A[right_pointer]] += 1;
            }
            // リセット
            else {
                cout << left_pointer << " " << right_pointer << endl;
                res_length = max(right_pointer - left_pointer + 1, res_length);
                // right_length だったものを left_length として取り扱う
                left_pointer += 1;
                mp[A[left_pointer]] -= 1;
                mp[A[right_pointer]] = 1;
            }
        }
        right_pointer += 1;
    }
    res_length = max(right_pointer - left_pointer + 1, res_length);

    cout << res_length << endl;
}