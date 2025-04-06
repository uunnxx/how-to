#include <stdio.h>
#include <stdlib.h>


int shortest_line_index(int lines[], int n) {
	int j;
	int shortest = 0; // int
	for (j = 1; j < n; j++) {
		if (lines[j] < lines[shortest]) {
			shortest = j;
		}
	}
	return shortest;
}


void solve(int lines[], int n, int m) {
	int i, shortest;

	for (i = 0; i < m; i++) {
		shortest = shortest_line_index(lines, n);
		printf("%d\n", lines[shortest]);
		lines[shortest]++;
	}
}


#define MAX_LINES 100

int main(void) {
	int lines[MAX_LINES];
	int n, m, i;
	scanf("%d%d", &n, &m);

	for (i = 0; i < n; i++) {
		scanf("%d", &lines[i]);
	}
	solve(lines, n, m);
	return 0;
}
