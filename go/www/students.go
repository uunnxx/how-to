package main

import ("fmt")


func main() {
    var student1 string = "John"  // type is string
    var student2 = "Jane"         // type is inferred
    x := 2                        // type is inferred


    var a string  // ""
    var b int     // 0
    var c bool    // false

    fmt.Println(a)
    fmt.Println(b)
    fmt.Println(c)
    
    fmt.Println(student1)
    fmt.Println(student2)
    fmt.Println(x)
}
