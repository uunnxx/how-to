#include <stdio.h>

// int main() {
// 	int integerType;
// 	float floatType;
// 	double doubleType;
// 	char charType;
//
// 	printf("Size of int: 	%ld byte\n", sizeof(integerType));
// 	printf("Size of float: 	%ld byte\n", sizeof(floatType));
// 	printf("Size of double: %ld byte\n", sizeof(doubleType));
// 	printf("Size of char: 	%ld byte\n", sizeof(charType));
//
// 	return 0;
// }
//
//
// struct car {
// 	char name[50];
// 	int year;
// 	float speed;
// } priora;
//
// priora.speed = 55;
//
// struct car *c = &priora; // записываем в с адрес priora
// c->speed = 55;





// int main() {
// 	double a, b, temp;
//
// 	printf("Enter a: ");
// 	scanf("%lf", &a);
//
// 	printf("Enter b: ");
// 	scanf("%lf", &b);
//
// 	temp = a;
// 	a = b;
// 	b = temp;
//
// 	printf("\nAfter replacing a = %.2lf\n", a);
// 	printf("\nAfter replacing b = %.2lf\n", b);
//
// 	return 0;
// }

int main() {
	int n, i;

	long long int sum;

	printf("Enter n: ");
	scanf("%d", &n);

	i = 1;
	while ( i <= n ) {
		sum += i;
		++i;
	}
	printf("Sum = %lld\n", sum);

	return 0;
}
