// Allows the file to be run by itself after compiling, SEE: https://golang.org/doc/code.html#PackageNames
package main

//import statements are similar to python syntax
import "fmt"

// This is the 'full' syntax for declaring a variable, NOTE: because go is statically typed a type MUST be provided
var greeting string = "Hello,"

// In go a main function is automatically called.
func main() {
	/**This is the shortform syntax for declaring a variable. It infers the type automatically, but still
	adheres to the precepts of static typing; NO implicit type casting.
	NOTE: This only works INSIDE functions, you cannot define global scope variables this way*/
	name := "John Doe"
	greet(name, greeting)
}

// A simple function declaration that takes two parameters and prints them
func greet(name string, greeting string) {
	fmt.Println(greeting, name)
}
