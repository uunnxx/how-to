module main

fn main() {
	println('Hello World!')
}


// Note the (important) difference between := and =.
// := is used for declaring and initializing, = is used for assigning.

fn main() {
	age = 21
}

// This code will not compile, because the variable age is not declared.
// All variables need to be declared in V.

fn main() {
	age := 21
}



mut a := 0
mut b := 1

println('${a}, ${b}') // 0, 1

a, b = b, a

println('${a}, ${b}') // 1, 0
