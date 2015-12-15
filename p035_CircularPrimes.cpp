#include <cmath>
#include <vector>
#include <deque>
#include <cstdio>

using namespace std;

bool check(int i);
int tenTo(int exponent);

vector<bool> sieve (10000001, true);

int main() {
	for (int i=2; i <= sqrt(10000001); i++) {
		if (sieve[i] == true) {
			for (int j = (i * i); j <= 10000001; j += i) {
				sieve[j] = false;
			}
		}
	}
	int count = 0;
	for (int i=100; i < 1000000; i++) {
		if (sieve[i] == true) {if (check(i) == true) {count ++;}}
	}
	count += 13;
  printf("%d\n", count);
	return 0;
}

bool check(int value) {
	int magnitude = 0;
	deque<int> digits;
	while (tenTo(magnitude) <= value) {
		magnitude++;
	}
	magnitude--;
	int n = value;
	for (int i = 0; i <= magnitude; i++) {
		digits.push_front(n%10);
		n /= 10;
	}
	int count = 0;
	int sum;
	for (int i = 0; i < magnitude; i++) {
		digits.push_back(digits.front());
		digits.pop_front();
		sum = 0;
		for (int j = 0; j <= magnitude; j++) {
			sum += digits.at(j) * tenTo(magnitude - j);
		}
		if (sieve.at(sum) == true) {count++;}
	}
	if (count == magnitude) {return true;}
	return false;
}

int tenTo(int exponent) {
	int total = 1;
	for (int i = 1; i <= exponent; i++) {
		total *= 10;
	}
	return total;
}
