#include <iostream>
#include <vector>
#include <utility>

using namespace std;

pair<vector<bool>, vector<int>> sieve(int max) {
  int limit = max + 1;
  vector<bool> s = vector<bool>(limit);
  vector<int> p {}; 

  for (int i = 0; i < limit; i++) {
    s[i] = true; 
  }

  s[0] = false;
  s[1] = false;

  for (int i = 2; i < limit; i++) {
    if (s[i]) {
      p.push_back(i);
      for (int j = i + i; j < limit; j += i) {
        s[j] = false;
      }
    }
  }

  return make_pair(s, p);
}

int main() {
  int upper_limit = 1000000;
  auto res = sieve(upper_limit); 
  vector<bool> s = res.first;
  vector<int> p = res.second;
  vector<int> sums {}; 

  int total = 0;
  for (int i : p) {
    sums.push_back(total);
    total += i;
  }
  sums.push_back(total);

  int max_sum = 0;
  int max_length = 0;
  
  for (int start = 0; start < sums.size(); start++) {
    for (int end = start + 1; end < sums.size(); end++) {
      int sum = sums[end] - sums[start];           
      if (sum > upper_limit) { break; }
      if (s[sum]) {
        int length = end - start;
        if (length > max_length) {
          max_sum = sum;
          max_length = length;
        }
      }
    }
  }
  
  cout << max_sum
       << endl;
}
