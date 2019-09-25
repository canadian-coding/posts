# Basic Logging in Go

## Description

Logging is the act of generating logs from a program. These are typically stored in a file or sent to a terminal to give developers a good idea of what's going on in their program at any given time.

## Definitions

### Logging

Logging is the act of generating logs from a program. The [logging Package](https://golang.org/pkg/log/) is the standard way of doing this in Go.

=====EXAMPLE HERE=====

```go
import "log"
```

## Usage

### Running

All of the code in the demo requires no external dependencies, it can be run by using one of two methods:

1. You can run the file directly via ```go run loggingDemo.go```
2. You can compile the file using ```go build loggingDemo.go``` then run the resulting binary (.exe on windows, and regular binary on mac/linux).

## Real World Applications

Logging is incredibly useful for debugging down the road, especially if you are running a very complicated app with many modules and files as hand debugging becomes genuinely impossible sometimes. It also helps you to understand what went wrong in edge cases when end users don't necessarily remember exactly what they did to break something.

## Additional info

===ADD ADDITIONAL INFO HERE===
