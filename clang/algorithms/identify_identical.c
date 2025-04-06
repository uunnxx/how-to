#include <stdio.h>
#include <stdlib.h>


void identify_idenctical(int values[], int n) {
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = i+1; j < n; j++)  {
			if (values[i] == values[j]) {
				printf("Twin integers found.\n");
				return;
			}
		}
	}

	printf("No two integers are alike.\n");
}


int identical_right(int snow1[], int snow2[], int start) {
	// Error!
	int offset;
	for (offset = 0; offset < 6; offset++) {
		if (snow1[offset] != snow2[start + offset])
			return 0;
	}
	return 1;
}


int  identical_right2(int snow1[], int snow2[], int start) {
	int offset, snow2_index;
	
	for (offset = 0; offset < 6; offset++) {
		snow2_index = start + offset;
		if (snow2_index >= 6) {
			snow2_index = snow2_index - 6;
			if (snow1[offset] != snow2[snow2_index]) {
				return 0;
			}
		}
	}
	return 1;
}


int identical_right3(int snow1[], int snow2[], int start) {
	int offset;
	for (offset = 0; offset < 6; offset++) {
		if (snow1[offset] != snow2[(start + offset) % 6]) {
			return 0;
	  	}
	}
	return 1;
}


int identical_left(int snow1[], int snow2[], int start) {
	int offset, snow2_index;

	for (offset = 0; offset < 6; offset++) {
		snow2_index = start - offset;
		if (snow2_index < 0)
			snow2_index = snow2_index + 6;
		if (snow1[offset] != snow2[snow2_index])
			return 0;
	}
	return 1;
}


int are_identical(int snow1[], int snow2[]) {
	int start;
	for (start = 0; start < 6; start++) {
		if (identical_right3(snow1, snow2, start))
			return 1;
		if (identical_left(snow1, snow2, start))
			return 1;
	}
	return 0;
}


void identify_idenctical2(int snowflakes[][6], int n) {
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = i+1; j < n; j++) {
			if (are_identical(snowflakes[i], snowflakes[j])) {
				printf("Twin snowflakes found.\n");
				return;
			}
		}
	}
	printf("No two snowflakes are alike.\n");
}


#define SIZE 100000


int main2(void) {
	static int snowflakes[SIZE][6];
	int n, i, j;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		for (j = 0; j < 6; j++) {
			scanf("%d", &snowflakes[i][j]);
	  	}
	}
	identify_idenctical2(snowflakes, n);
	return 0;
}


int main(void) {
	int a[5] = {1, 2, 3, 1, 5};
	identify_idenctical(a, 5);
	return 0;
}
