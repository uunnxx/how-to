#include <stdio.h>


int main(int argc, char *argv[]) {
	char *name1 = "Brice";

	printf("%s\n\n", name1);

	char *name2 = name1;

	printf("name1 --> %p\n", name1);
	printf("name2 --> %p\n\n", name2);

	name2 += 2;

	printf("%s\n\n", name1);


	printf("name1 --> %p\n", name1);
	printf("name2 --> %p\n\n", name2);

	*name2 = 'y';

	printf("%s\n\n", name1);

	printf("name1 --> %p\n", name1);
	printf("name2 --> %p\n\n", name2);

	printf("%s\n", name1);
}
