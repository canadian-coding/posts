# Processing Language Overview

![Processing Logo](https://upload.wikimedia.org/wikipedia/commons/2/2e/Processing_3_logo.png)

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
- Created: 2001

## Useful Starter Resources

...

### ^^ TODO ^^

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
* @author: Canadian Coding
* @param: xpos The x position of the ball
* @param: ypos The y position of the ball
* @param: velocity The velocity of the ball
*/
class Ball{
    int xPos, yPos, velocity; //
    Ball(int xPos, int yPos, int velocity){
        self.xPos = xPos;
    }
}
```

  ### ^^ TODO ^^



## Variables & Typing

...

### ^^ TODO ^^

## Functions

...

### ^^ TODO ^^

## Running Processing Code

...

### ^^ TODO ^^