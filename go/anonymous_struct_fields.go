package main

import (
    "fmt"
)


func main() {
    animals := struct {
        int
        string
    }{1, "Dog"}

    fmt.Println(animals.int)
    fmt.Println(animals.string)
}
