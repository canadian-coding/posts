package main // Allows file to be run on it's own

import "fmt" // Used to print to stdout

// Currency is a dummy type for the enumerator found below
type Currency int

// An enumerator of various currencies
const (
	// NOTE: iota starts at 0 and increments on every definition until the next const()
	CAD Currency = iota // CAD == 0
	USD Currency = iota // USD == 1
)

// Function takes a Currency as an argument and returns a string representation
func (currency Currency) String() string {
	// Define an array of strings to print based on the enumerator definition
	names := [...]string{
		"CAD", // If the currency passed is equal to 0 return CAD
		"USD"} // If the currency passed is equal to 1 return USD

	return names[currency] // return the name of currency
}

// Prints the string and int representations of Currency values
func main() {
	fmt.Printf("%s is equivalent to %d\n%s is equivalent to %d",
		Currency(0), Currency(0), Currency(1), Currency(1))
}
