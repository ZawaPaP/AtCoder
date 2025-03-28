#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  vector<int> v(n);

  for (int i; i < n; i++)
   cin >> v.at(i);
  
  set<int> s;
  
  for (auto i: v) {
    s.insert(i);
  }
  
  cout << s.size() << endl;
  return 0;
}