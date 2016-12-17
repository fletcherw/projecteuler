#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main() {
  vector<int> counts = vector<int>(1001);

  int count = 0; 
  for (int a = 1; a < 250; a++) {
    for (int b = a; b < 500; b++) {
      for (int c = b; a + b + c <= 1000; c++) { 
        if (a*a + b*b == c*c) {
          counts[a+b+c]++;
        }
      }
    }
  }

  int max = 0;
  int max_ind = 0;
  for (int p = 12; p <= 1000; p++) {
    if (counts[p] > max) { 
      max_ind = p;
      max = counts[p];
    }
  }

  cout << max_ind << endl;
}

