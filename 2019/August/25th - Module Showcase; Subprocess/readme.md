# Module Showcase; subprocess

## Description

Subprocess is a way to run executable files and binaries in python (including other python files). It is an incredibly useful tool for setup scripts, project build scripts, and other complicated tasks.

## Definitions

### Subprocess

A python module that allows you to run subprocesses to complete tasks such as running executable files, binaries, and even other python files.

A basic example would be to run another python file from a python file:

```python
import subprocess

# Instantiates another python interpreter inside the current session and runs other_python_file.py
subprocess.run(["python", "other_python_file.py"])
```

You could also use it to run files in other languages like Go. Here is an example go file to run:

```helloWorld.go```

```go
import "fmt"

func main(){
    fmt.Print("Hello World!")
}
```

This file can then be run in python using:

```python
import subprocess

# Equivalent to running go run helloWorld.go
subprocess.run(["go", "run", "helloWorld.go"])
```

Files that are in other directories can be run by pathing the final argument to the correct file, for example:

```python
import subprocess

# Equivalent to running go run helloWorld.go, and assumes it is 3 directories deep
subprocess.run(["go", "run", "/path/to/file/helloWorld.go"])
```

## Usage

### Running

In this repo there are two demos you can run;

#### Subprocess Demo

1. You can run the basic demo by ```python subprocess_demo.py``` or ```python3 subprocess_demo.py```

#### C Demo

1. First cd into the ```/c_demo``` folder.
2. run  ```python cross_language_demo.py``` or ```python3 cross_language_demo.py```

## Real World Applications

Python subprocesses are incredibly useful for writing scripts that need to interface with non-python executable files and/or binaries. For example if you have a project that is cross-language (let's say a backend in Go and Rust, with a frontend that needs a webpack build), you can run all the necessary migrations, dependency fetching, compiling, and running from a single python script.

## Additional info

[Python 3 reference for subprocess module](https://docs.python.org/3/library/subprocess.html)
