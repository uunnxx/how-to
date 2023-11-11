module main

fn main() {
	os := $if windows { 'Windows' } $else { 'Unix' }

	println('Hello, $os user!')
}
