#include <iostream>
#include <limits>
#include <cmath>
#include <cassert>

using namespace std;
using nt = long int;

constexpr double epsilon = 0.00001;

inline nt pent(int n) {
  return n * (3 * n - 1) / 2; 
}

inline bool is_pent(int x) {
  double root = sqrt(1.0 + 24.0 * x);
  bool is_square = fabs(root - round(root)) < epsilon;
  int int_root = (int) root;  
  return is_square && (int_root % 6 == 5);
}

int main() {
  nt min_d = -1; 

  for (nt j = 1; j < 100000; j++) {
    for (nt k = j+1; k < j + 100000; k++) {
      nt sum = pent(j) + pent(k); 
      nt diff = pent(k) - pent(j); 
      if (min_d != -1 && diff > min_d) break;

      if (is_pent(sum) && is_pent(diff)) {
        if (min_d = -1 || diff < min_d) { 
          min_d = diff;
        }
      }
    }
    nt diff = pent(j+1) - pent(j); 
    if (min_d != -1 && diff > min_d) { break; }
  }
  
  cout << min_d << endl;
}
