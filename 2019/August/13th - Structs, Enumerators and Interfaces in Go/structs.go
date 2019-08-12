package main // Allows file to be run on it's own

import "fmt" // Used to print to stdout

// A Struct to represent coins in various currencies
type Coin struct { // NOTE: Structs are like objects that only have attributes
	value int    // How much the coin is worth in cents as an int
	name  string // The colloquial name of the coin
}

// Creates all the coins found in CAD currency, adds them to a list then iterates and prints their values
func main() {
	// All CAD coins NOTE: Value is in cents so for example a toonie($2) is 200
	var coins []Coin // Instantiate a slice of unknown length, containing coins
	toonie := Coin{value: 200, name: "Toonie"}
	loonie := Coin{value: 100, name: "Loonie"}
	quarter := Coin{value: 25, name: "Quarter"}
	dime := Coin{value: 10, name: "Dime"}
	nickle := Coin{value: 5, name: "Nickle"}
	coins = append(coins, toonie, loonie, quarter, dime, nickle) // Fill the slice with the Coin's

	fmt.Printf("The coins in CAD are:\n")
	for _, currentCoin := range coins { // For loop to print coin information
		fmt.Printf("Coin name: %v \nCoin Value (in cents): %v\n",
			currentCoin.name, currentCoin.value)
	}

}
