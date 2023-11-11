#include <stdio.h>


int loop_(int arg) {
	int i = 0;

	while (true) {
		if (i >= arg) {
			break;
		}
		printf("%d\n", i);
		i++;
	}

	return 0;
}


int main() {
	int a, b, res;
	a = 10;
	b = 5;

	res = (a > b) ? a : b;

	printf("res=%d\n", res);

	loop_(res);

	return 0;
}
