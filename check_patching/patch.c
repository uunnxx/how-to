#include <stdio.h>


int main() {
	FILE *f = fopen("main", "r+b");
	unsigned char opcode = 0x74;
	fseek(f, 0x1184, SEEK_SET);
	fwrite(&opcode, sizeof(opcode), 1, f);
	fclose(f);
	printf("Done!\n");
	return 0;
}
