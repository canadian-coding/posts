package main

import "fmt" // More info about % operators can be found here: https://golang.org/pkg/fmt/

// Coin is a struct to represent coins
type Coin struct {
	value int    // How much the coin is worth in cents as an int
	name  string // The colloquial name of the coin
}

// A function showing off print formatting with
func main() {
	// Example of formatting with ints
	number := 3
	fmt.Printf("Value of number: %d", number)

	// Example of formatting with floats
	pi := 3.14159
	fmt.Printf("\nValue of pi: %f", pi)

	// Example of formatting with strings
	greeting := "Hello World!"
	fmt.Printf("\nValue of greeting: %s", greeting)

	// Example of formatting with struct instances
	quarter := Coin{value: 25, name: "Quarter"} // Printing a struct instance prints it's values
	fmt.Printf("\nValues of a quarter: %v\nValues of a quarter with field names: %+v",
		quarter, quarter)

	// Example of printing what variables types are
	fmt.Printf("\nThe types of number, greeting and quater are %T, %T, and %T",
		number, greeting, quarter)
}
