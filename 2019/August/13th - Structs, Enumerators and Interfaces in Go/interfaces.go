package main // Allows file to be run on it's own

import "fmt" // Used to print to stdout

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

// Instantiates a coin and runs the toUSD function
func main() {
	toonie := Coin{value: 2.00, name: "Toonie"}
	fmt.Printf("One %v is worth CAD $%v and USD $%v",
		toonie.name, toonie.value, toonie.toUSD())
}
