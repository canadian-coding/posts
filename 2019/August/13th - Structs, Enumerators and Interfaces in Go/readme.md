# Structs, Enumerators and Interfaces in go

## Description

Structs, Enumerators and Interfaces are various different types/data structures that can be created in go to fulfill various needs. These three mechanisms are the closest that go gets to being object oriented **BUT** make no mistake, none of these types are similar to traditional object oriented programming entirely, instead they allow you to follow similar design patterns that are available in object oriented languages without any sort of real sub-classing, or any 'one-stop shop' for objects.

## Definitions

### Types

Types are a way of generalizing data; for example a real number can be represented as an integer type (or int as it's commonly called). Types are found in all languages from simple types like integers, and strings to collections like arrays to even custom types like those presented in this demo.

### Structs

Structs are a way of defining custom typed groupings of data (similar to class attributes). Another easy way to think about structs is to think of them is similar to a templated version of a [Hash table](https://en.wikipedia.org/wiki/Hash_table) (a dict in python).


A simple example would be a date struct:

```go
type Date struct{
    day int
    month int
    year int
}
```

You can then use this date struct as a type to store data, for example:

```go
package main

import "fmt"

func main(){
    today := Date{day: 13, month: 8, year: 2019}
    // The data can then be accessed using dot syntax
    fmt.printf("Today is %v-%v-%v", today.day, today.month, today.year) // prints Today is 13-8-2019
    }
```

Because structs are types you can use them in almost any way you would use any other type such as creating an array of them, or nesting them inside each other. 
To demonstrate the nesting capabilities here is an example of a person struct with an attribute of birthday that is of the custom struct type Date that we defined earlier:

```go
type Person struct{
    name string
    age int
    birthday Date
}
```

### Interfaces

Interfaces are collections of method signatures that you can assign a name to. They effectively allow you to store a set of methods that will be implemented later on, usually in the context of a struct. For example:

``` go
// Coin is a Struct to represents coins in various currencies
type Coin struct { // NOTE: Structs are like objects that only have attributes
    value float64 // How much the coin is worth
    name  string  // The colloquial name of the coin
}

// Currency is an interface that stores Currency conversion functions
type Currency interface {
    toUSD() float64
}

// toUSD takes a coin in CAD and returns the USD equivalent
func (c Coin) toUSD() float64 {
    return c.value * 0.7 // 1 CAD is roughly .7 USD
}
```

With this interface of Currency added to the Coin struct, we can now do something like this:

```go
toonie := Coin{value: 2.00, name: "Toonie"}
fmt.Printf("One %v is worth CAD $%v and USD $%v", toonie.name, toonie.value, toonie.toUSD()) // prints One toonie is worth CAD $2 and USD $1.4
```

Notice that the interface allows us to use the dot syntax to pass the instance as an argument, this is incredibly helpful for readability in programs with complicated structs and interfaces.

### Enumerators

Enumerators are data structures that allow you to store **CONSTANT** information in a structured way. The idea behind enumerators is to store values that will be used throughout a program in a codified way to provide consistent behaviour. Typically enumerators represent data as key-value pairs where the value is an int. For example you could create an enumerator for various countries:

```go
// Countries is a dummy type for the enumerator found below
type Countries int

// An enumerator of various countries
const (
    Canada Countries = 0
    UnitedStates Countries = 1
)
```

There is also a mechanism called iota built into go to make creating enumerators more simple. Iota will start as 0 right after the const() and increment on every assignment.

Here is an example of how it works:

```go
// Countries is a dummy type for the enumerator found below
type Countries int

// An enumerator of various countries
const (
    Canada Countries = iota // iota is == 0
    UnitedStates Countries = iota // iota == 1
)

// The enumerator above is equivalent to
const (
    Canada Countries = 0
    UnitedStates Countries = 1
)
```

You can also create a function to print string representations of your enumerators, for example:

```go
package main

import "fmt"

// Countries is a dummy type for the enumerator found below
type Countries int

// An enumerator of various countries
const (
    Canada Countries = 0
    UnitedStates Countries = 1
)

// Function takes a Countries instance as an argument and returns a string representation
func (country Countries) String() string {
    // Define an array of strings to print based on the enumerator definition
    names := [...]string{
        "Canada", // If the country passed is equal to 0 return Canada
        "United States"} // If the country passed is equal to 1 return United States

    return names[country] // return the name of country
}

func main(){
    // Prints the string representation of Countries(0), which is canada
    fmt.Printf("My country is %s", Countries(0))
}
```

## Usage

### Running

You can run each of the demos by using one of two methods:

1. You can run the file directly via ```go run <file>.go```
2. You can compile the file using ```go build <file>.go``` then run the resulting binary (.exe on windows, and regular binary on mac/linux).

## Real World Applications

The real world applications of Structs, Enumerators and Interfaces are endless as such I will just leave you with the examples provided, and some additional resources to learn about each.

### Additional information

Here are some resources with more examples and information:

- [Structs](https://gobyexample.com/structs)
- [Enumerators](https://blog.learngoprogramming.com/golang-const-type-enums-iota-bc4befd096d3)
- [Interfaces](https://gobyexample.com/interfaces)
