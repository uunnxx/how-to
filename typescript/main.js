var user = {
    firstName: "Angela",
    lastName: "Davis",
    role: "Professor"
};
console.log(user.lastName);
function add(a, b) {
    return a + b;
}
console.log(add(64, 2));
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 4] = "Blue";
})(Color || (Color = {}));
var c = Color.Green;
