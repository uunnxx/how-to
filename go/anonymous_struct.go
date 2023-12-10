package main

import (
    "fmt"
)


func main() {
    Animal := struct {
        Kind string
        Diet string
    }{"Dog", "Omnivorous"}

    fmt.Println(Animal.Kind, "-", Animal.Diet)
}
