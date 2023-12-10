package main

import "fmt"


type Animal struct {
    Kind string
    Diet string
}

type Owner struct {
    Name string
    Country string
}

type Dog struct {
    *Animal
    *Owner
    Name string
    Breed string
}

type Cat struct {
    *Animal
    *Owner
    Name string
    Breed string
}


func main() {
    var dog Dog

    dog.Name = "Maximus"

    dog.Animal = &Animal {
        Kind: "Dog",
        Diet: "Omnivorous",
    }

    dog.Breed = "Pitbull"

    dog.Owner = &Owner {
        Name: "John",
        Country: "USA",
    }

    fmt.Printf("Name of %s is %s\n", dog.Animal.Kind, dog.Name)
    fmt.Printf("%s is a %s with an %s diet\n", dog.Name, dog.Breed, dog.Animal.Diet)
    fmt.Printf("%s is owned by %s who lives in %s\n", dog.Name, dog.Owner.Name, dog.Owner.Country)
}
