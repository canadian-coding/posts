# Processing Language Overview

<img src="https://upload.wikimedia.org/wikipedia/commons/2/2e/Processing_3_logo.png" alt="Processing logo" height="450" width="450">

Processing is not so much a language as it is a drawing and graphics library. In fact Processing supports multiple different languages (Java, javascript, python). But for the most part when people are talking about 'processing' what they really mean is the processing library that's built on top of Java that includes it's own IDE (integrated development environment), and so that is what this post refers to.



> Processing is a flexible software sketchbook and a language for learning how to code within the context of the visual arts. Since 2001, Processing has promoted software literacy within the visual arts and visual literacy within technology. There are tens of thousands of students, artists, designers, researchers, and hobbyists who use Processing for learning and prototyping.

-From https://processing.org/ homepage

## Table of Contents
<!-- TOC -->

- [Processing Language Overview](#processing-language-overview)
  - [Table of Contents](#table-of-contents)
  - [Language Properties](#language-properties)
  - [Useful Starter Resources](#useful-starter-resources)
  - [Comments/Documentation](#commentsdocumentation)
  - [Variables & Typing](#variables--typing)
  - [Functions](#functions)
  - [Running Processing Code](#running-processing-code)

## Language Properties

- Typing : Statically Typed, Strongly typed
- Paradigms: Multiparadigm;
  - Imperative
  - Concurrent
  - Object oriented
  - Functional
  - etc.
- Semi-colon based line endings (need to put a ';' after every statement)
- Created: 2001

## Useful Starter Resources

[Hello Processing](https://hello.processing.org/)

[Processing tutorials list](https://processing.org/tutorials/)

[processing examples list](https://processing.org/examples/)

[Processing Books list](https://processing.org/books/)

[Processing reference docs](https://processing.org/reference/)

*Because processing is built on top of java most java resources will also be useful for processing.*

## Comments/Documentation

The commenting system in Processing is pretty standard, below are examples of single and multiline comments.

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

Docstrings, or document comments as they are called in java (and by extension processing) are formatted as multiline comments **Before** a function/class definition, and even feature [metadata](https://en.wikipedia.org/wiki/Javadoc#Table_of_Javadoc_tags).

Here is an example:

```java
/**
* A class that represents a ball
* @author Canadian Coding
* @param xpos The x position of the ball
* @param ypos The y position of the ball
* @param velocity The velocity of the ball
*/
class Ball{
    int xPos, yPos, velocity; //
    Ball(int xPos, int yPos, int velocity){
        self.xPos = xPos;
    }
}
```



## Variables & Typing

Since processing is based on Java it  is a statically typed and strongly typed language; This means that you must declare variables types (int, string etc.) when you initialize variables, and that variable types cannot be changed implicitly.



There are two syntactically distinct ways to create variables in processing:

1. Instantiate a variable, then assign a value:

```java
String greeting;
greeting = "Hello";
```

2. Instantiate a with a value:

```java
String greeting = "Hello";
```



## Functions

Functions in processing (as they do in java) require an explicit statement of each parameter type, as well as the return type (if there is one).



*Note if you are familiar with java that the syntax for public/private functions is optional and will default to public if not specified*



Generally the format is as follows:

```java
/** Docstring goes here*/
returnType functionName(parameterType parameterName){
    ...			// Some code here
    return foo  // Return something of the correct returnType
}
```



For example:

```java
/** A function that takes in a square's length/height and returns it's perimeter
* @param x The length/height of the square
* @return The perimeter of a square with length x
*/
int squarePerimeter(int x){
    int perimeter = x * 4; // Multiply x value by 4
    return perimeter;
}
```



## Running Processing Code

Processing code is saved in .pde files **inside a directory** of the same name, these files can be run from the IDE by opening them up and clicking the play Icon in the [IDE](https://processing.org/download/). 



I have created a demo that draws 3 snowmen. The demo illustrates the use of:

1. Variables
2. Functions
3. For loops
4. The setup and draw methods



To run the demo code in this repository simply change directories into the ```/processingDemo``` folder and open the ```processingDemo.pde``` file inside the processing [IDE](https://processing.org/download/) and hit the play icon in the top left. 