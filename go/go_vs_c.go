package main

import "fmt"


// Here's an example of a basic function in C/C++, to perform squaring of an integer:

// int Square (int n)
// {
//		return n * n;
// }

// And here's that same function in Go:

func Square(n int) int {
	return n * n
}

func main() {
    fmt.Println(Square(4))
}

