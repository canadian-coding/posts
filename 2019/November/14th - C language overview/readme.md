# C Language Overview



C is a general purpose language primarily used in low-level programming such as operating system code. It was originally designed to help create Unix software by bell labs (Dennis Ritchie specifically), but nowadays is found in many operating systems and pieces of software. 



## Table of Contents

<!-- TOC -->

- [C Language Overview](#C-language-overview)
    - [Table of Contents](#table-of-contents)
    - [Language Properties](#language-properties)
    - [Useful Starter Resources](#useful-starter-resources)
    - [Comments/Documentation](#commentsdocumentation)
    - [Variables & Typing](#variables--typing)
    - [Functions](#functions)
    - [Running C Code](#running-C-code)

## Language Properties

- Typing : Statically Typed, Weakly Typed
- Paradigm: Procedural
- Semi-colon based line endings (need to put a ';' after every statement)
- Created: 1972



## Useful Starter Resources

[C programming language (book)]( https://www.amazon.ca/Programming-Language-2nd-Brian-Kernighan/dp/0131103628/ref=sr_1_1?crid=2NS9YMQCV2TG9&keywords=the+c+programming+language&qid=1573684591&sprefix=the+c+pro%2Caps%2C226&sr=8-1 )

[Tutorialspoint]( https://www.tutorialspoint.com/cprogramming/index.htm )

[learn-c]( https://www.learn-c.org/ )



## Comments/Documentation

The commenting system in C is pretty standard, below are examples of single and multiline comments.

```java
// This is a single line comment

/**
This
is
a
multiline
comment
*/
```

Docstrings are possible (and recommended), but have no officially recognized structure. I have included an example of a function docstring with my preferred style, which is modelled after the [python numpy style]( https://numpydoc.readthedocs.io/en/latest/format.html )(there is also the one outlined [here]( https://www.cs.swarthmore.edu/~newhall/unixhelp/c_codestyle.html ) that is quite good).

Here is an example:

```c
#include <math.h>

/** Calculates the area of a circle and returns it based on radius
* 
* Parameters
* ----------
* radius: 
*		  The radius of the circle you want the area of.
* 
* Returns
* -------
* The area of a circle with the given radius as an int
*/
int area_of_circle(int radius){
  int area = M_PI * (radius*radius); // pi times radius squared
  return area;
  }
```



## Variables & Typing

Since C is a statically typed and Weakly typed language; This means that you must declare variables types (int, float etc.) when you initialize variables, and that variable types can be manipulated more easily than strongly typed languages.



There are two syntactically distinct ways to create variables in C:

1. Instantiate a variable, then assign a value:

```java
int age;
age = 21;
```

2. Instantiate a variable with a value:

```java
int age = 21;
```



Since I mentioned that C is weakly typed here is an example of converting a float to an int in C:

```c
float age = 21.45;

age = (int)age; // Now equal to the int 21
```



## Functions

Functions in C require an explicit statement of each parameter type, as well as the return type (if there is one).



Generally the format is as follows:

```c
/** Docstring goes here*/
return_type function_name(parameter_type parameter_name){
    ...			// Some code here
    return foo; // Return something of the correct return type
}
```



For example:

```c
#include <math.h>
/** Calculates the area of a circle and returns it based on radius
* 
* Parameters
* ----------
* radius: 
*		  The radius of the circle you want the area of.
* 
* Returns
* -------
* The area of a circle with the given radius as an int
*/
int area_of_circle(int radius){
  int area = M_PI * (radius*radius); // pi times radius squared
  return area;
  }
```



## Running C Code

To run C code you will need a C compiler, here are a few possible options:

[gcc]( https://gcc.gnu.org/ ) (What I use)

[clang]( https://clang.llvm.org/ )



Assuming you installed gcc you can compile the code using:



```bash
gcc <filename>.c -o <executeable name>
```



 This will then compile the code to a binary (.exe for windows, and regular binary for macOS & Linux) and run it.
