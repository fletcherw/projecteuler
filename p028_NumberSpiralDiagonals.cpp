#include <cstdio>

int main() {
	int sum = 0;
	for (int i = 1; i <= 500; i++) {
		int k = (2 * i) + 1;
		sum += (k * k * 4) - (i * 12);
	}
	sum ++;
  printf("%d\n", sum);
}
