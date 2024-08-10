#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct NODE_TYPE *load_data(const char *path) {

	FILE *file = fopen(path, "rb");

	if (file == NULL) {
		printf("Unable to open %s for reading\n", path);
		exit(1);
	}

	fseek(file, 0L, SEEK_END);
	size_t size = ftell(file);
	fseek(file, 0L, SEEK_SET);



};



int main(int argc, char *argv[]) {
	printf("Some output!");
}
