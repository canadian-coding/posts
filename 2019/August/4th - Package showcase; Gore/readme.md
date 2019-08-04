# Package Showcase; Gore

## Description

Gore is a Go REPL that allows you to do an interactive coding session.

## Definitions

### Gore

A REPL for Go; [Source](https://github.com/motemen/gore).

### REPL; Read Eval Print Loop

An interactive coding environment. A REPL allows you to type code directly into a terminal (or [webpage](https://repl.it/)) and run code. This is incredibly useful for testing something small out in a language, or for teaching purposes.

## Usage

To run gore you need to follow the steps outlined in the [install guide](https://github.com/motemen/gore#installation).

### Running

After installation you can use gore by running ```gore``` from your command line. See [Usage Docs](https://github.com/motemen/gore) for details.

## Real World Applications

Gore (and REPL's more generally) are incredibly useful for testing small chunks of code and/or for teaching people with small snippets of code.

## Additional information

Gore does have some weird syntax differences from go in some cases. Imports for example are done via:

``` go
:import "fmt" // Notice the colon before the import statement
```

There are also some weird runtime behaviours. Gore behaves similarly to main package programs in go. Any main function defined (or the first function in the case of no main function definition) will be run automatically on every statement (like a Comment or function definition).
