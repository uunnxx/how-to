#include <stdio.h>


struct color {
	int R;
	int G;
	int B;
};

struct color red={ .R=255 };
struct color green={ .G=255 };
struct color blue={ .B=255 };


void print_color_code (struct color *c) {
	printf("%d %d %d\n", c->R, c->G, c->B);
}

int main() {
	print_color_code(&red); // R
	print_color_code(&green); // G
	// or
	// print_color_code(&(struct color){ .G=255 });
	print_color_code(&blue); // G
}
