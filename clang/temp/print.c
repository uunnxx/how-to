#include <stdio.h>


/*
 *
 *
*/

int main() {
	printf("Print some text!\n");
	printf("Print some text!\n");

	int x;
	x = 111;
	int y = 222;
	float p = 1.05;
	char h = 'H';
	char name[] = "String";

	printf("\n");


	// %d for bool (1 byte) [#<stdbool.h>]

	printf("int x: %d\n", x);  //
	printf("int y: %d\n", y);
	printf("float p: %f\n", p); // %f for 4 bytes (32 bit of precision)
	printf("float p: %lf\n", p); // %lf for 8 bytes (64 bit of precision)
	printf("char H: %c\n", h);
	printf("char[] name: %s\n", name);

	return 0;
}
