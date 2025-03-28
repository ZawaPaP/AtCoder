#include <bits/stdc++.h>
using namespace std;

vector<int> create_temp(int N, int control_num){
    vector<int> temp(N);
    int push_num = 1;
    for (int i = 1; i <= N; ++i)
    {
        if (i == control_num)
            push_num += 1;
        temp.push_back(push_num);
        push_num += 10;
    }
}

    int main()
{
    int N, M;
    cin >> N >> M;

    vector<vector<int>> A;

    vector<int> temp(N);

    int push_num = M;
    for (int i = N - 1; i >= 0; ++i)
    {
        temp[i] = push_num;
        push_num -= 10;
    }

    // 操作している桁数
    int control_num = N;

    while (temp[control_num - 1] < M) {
        A.push_back(temp);
        // 今の最後の桁に + 1 して再度試す
        temp[control_num - 1] += 1;
    }

    // temp[control_num] = M の時も追加
    A.push_back(temp);

    // 位を1つ下げ る
    control_num -= 1;

    // tempを作成


    // 要素が M を超えた場合、1つ下の桁に１追加し、再度tempを作成
}