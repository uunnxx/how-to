#include <stdio.h>


// adds two to an integer and and returns the result
int adder(int a) {
	return a + 2;
}


int main() {
	int x = 40;
	x = adder(x);
	printf("x is: %d\n", x);

	return 0;
}
