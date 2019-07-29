# Go/Golang Language Overview

![Go Gopher by Renee French](https://golang.org/doc/gopher/gophercolor.png)
This is the Go Gopher a mascot for [golang](https://golang.org). It was developed by [Renee French](https://en.wikipedia.org/wiki/Ren%C3%A9e_French) for the language.

## Table of Contents
<!-- TOC -->
- [Go/Golang Language Overview](#gogolang-language-overview)
  - [Table of Contents](#table-of-contents)
  - [Language Properties](#language-properties)
  - [Useful Starter Resources](#useful-starter-resources)
  - [Comments/Documentation](#commentsdocumentation)
  - [Variables & Typing](#variables--typing)
  - [Functions](#functions)
  - [Running Go Code](#running-go-code)

## Language Properties

- Typing : Statically Typed, Strongly typed
- Paradigms: Multiparadigm;
  - Imperative
  - Concurrent
  - Object oriented
  - Functional
  - etc.
- Created: November 10 2009
- Used by:
  - Uber
  - Google
  - Twitch
  - Medium
  - [etc.](https://www.gowitek.com/golang/blog/companies-using-golang)

## Useful Starter Resources

[A list of first party documentation](https://golang.org/doc/)

[A tour of go (official interactive tour of the language)](https://tour.golang.org/welcome/1)

[Official Go (also called golang) Website](https://golang.org/)

[Go source code](https://github.com/golang/go)

[Go standard library source monorepo](https://github.com/golang)

[Effective Go (A sort of style/best practices guide)](https://golang.org/doc/effective_go.html)

## Comments/Documentation

The commenting system in Go is pretty standard, below are examples of single and multiline comments.

```go
// This is a single line comment

/**
This
is
a
multiline
comment
*/
```

Unlike python there is no explicit syntax for docstrings in go.

## Variables & Typing

Go is a statically typed and strongly typed language; This means that you must declare variables types (int, string etc.) when you initialize variables, and that variable types cannot be changed.

There are three syntactically distinct ways to create variables in Go:

The first is to instantiate with an explicit type and then assign a value

```go
var greeting string
greeting = "hello"
```

The second is to instantiate and assign a value all at once

```go
var greeting string = "hello"
```

The third is somewhat confusing and leads people to believe that Go is dynamically typed. The third can **ONLY** be used in functions and allows you to instantiate a variable without a specific type being **DECLARED**, the type is inferred from what you provide.

```go
func greet(name string){
    greeting := "Hello"
    fmt.Println(greeting, name) // prints Hello <Name>
}
```

## Functions

Below are examples of function declarations in Go, there are examples of functions with and without arguments:

```go
// An example of a function with no arguments provided
func hello_world(){
    fmt.Println("Hello World!")
}

// An example of a function that takes two arguments and prints them, remember you MUST specify argument type for each argument
func greet(name string, greeting string) {
    fmt.Println(greeting, name)
}
```

## Running Go Code

To run go code there are two options either:

1. Run ```go build <filename>``` then run the resulting .exe(windows)/binary(mac and linux) file.

2. Run ```go run <filename>```, this will run the code by compiling and running the result **but** it does not save the resulting .exe(windows)/binary(mac and linux) file.
