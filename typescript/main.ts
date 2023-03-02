const user = {
  firstName: "Angela",
  lastName: "Davis",
  role: "Professor"
}

console.log(user.lastName)

function add(a: number, b: number): number {
  return a + b
}

console.log(add(64, 2))


enum Color {Red, Green, Blue = 4}
let c: Color = Color.Green
