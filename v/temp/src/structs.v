struct Point {
	x int
	y int
}

mut p := Point {
	x: 10
	y: 20
}

println(p.x)
p = Point{10, 20}

assert p.x == 10
