# String Formatting in go

## Description

String formatting is an incredibly useful tool for building dynamic strings in Go programs. It will allow you to build strings using variable's as input.

## Definitions

### String Formatting

The process of dynamically building strings based on variables and preset values. For example, lets say you are bulding a client dashboard that displays a welcome message. For this you might want to create a greeting that is along the lines of:

```Hello <name> The weather today is <current_temperature> degrees. You have <email_count> new emails.```.

To do this you could do:

```go
name := "John Smith" // A dummy name
emailCount := 3 // A representation of users # of new emails
currentTemperature := 20.3567 // A representation of the current temperature in celsius
fmt.Printf("Hello, %s The weather today is %f degrees. You have %d new emails.",
    name, currentTemperature, emailCount)
```

Note that fmt.Printf() can be used to format and immediately print strings. You can also use fmt.Sprintf() to just build the string and use it later.

For example:

```go
name := "John Smith" // A dummy name
emailCount := 3 // A representation of users # of new emails
currentTemperature := 20.3567 // A representation of the current temperature in celsius
// Create greeting string to be used later
greeting := fmt.Sprintf("Hello, %s The weather today is %b degrees. You have %d new emails.",
    name, currentTemperature, emailCount)
```

## Usage

### Running

All of the code in the demo requires no external dependencies, it can be run by using one of two methods:

1. You can run the file directly via ```go run stringFormatting.go```
2. You can compile the file using ```go build stringFormatting.go``` then run the resulting binary (.exe on windows, and regular binary on mac/linux).

## Real World Applications

String formatting is used all over the place to do everything from welcome messages to system and program information output messages.
