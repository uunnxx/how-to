#include <stdio.h>


int f(void) {
	// int x = 5;
	static int x = 5;
	printf("%d\n", x);
	x++;

	return 0;
}


int main(void) {
	f();
	f();
	f();

	return 0;
}
