#include <math.h>
#include <stdio.h>

int main(void) {
	int i = 128;
	if (i == pow(2, 7)) {
		puts("equal");
	}
}


int factorial(int n) {
	if (n <= 1) return 1;
	else return n * factorial(n - 1);
}
