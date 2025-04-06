#include <stdio.h>
#include <stdlib.h>


int compare(const void *first, const void *second) {
	int i;
	const int *snowflakes1 = first;
	const int *snowflakes2 = second;

	if (are_identical(snowflakes1, snowflakes2)) {
		return 0;
	}

	for (i = 0; i < 6; i++) {
		if (snowflakes1[i] < snowflakes2[i])
			return -1;
	}
	return 1;
}
