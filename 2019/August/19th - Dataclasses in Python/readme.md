# Dataclasses in python

## Description

[Dataclasses](https://docs.python.org/3/library/dataclasses.html) are a simple way to define classes with many attributes.

## Definitions

### Dataclasses

[Dataclasses](https://docs.python.org/3/library/dataclasses.html) is a python standard library module for creating dataclasses. Dataclasses are just syntactically simpler class definitions, typically this is used when you have a class that is used to store many attributes to save you from having to type out ```__init__()``` and ```__repr__()``` methods for your classes. 

Consider the example below:

```python
from dataclasses import dataclass # import dataclass method from module

@dataclass # Decorate class to let python know this is a dataclass
class user:
    name: str
    age: int
    birthday: str
    family_names: list[str]
    address: str
    job_title: str
    country_of_birth: str
```

And the examples equivalent code without using dataclasses:

```python
class user:
    def __init__(self, name, age, birthday, family_names, address, job_title, country_of_birth):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.family_names = family_names
        self.address = address
        self.job_title = job_title
        self.country_of_birth = country_of_birth

    def __repr__(self):
        return f"user(name='{self.name}', age={self.age}, birthday = '{self.birthday}',family_names = '{self.family_names}', address='{self.address}', job_title='{self.job_title}', country_of_birth='{self.country_of_birth}' )"
```

13 lines vs 8, not to mention the fact that if any of the variables change, or the class is subclassed the ```__repr__``` method will need to be recreated from scratch (including the hardcoded single quotes around strings to indicate their types).

## Usage

### Running

In this repo you can see the demo code and actually run it by running ```python <filename>.py``` or ```python3 <filename>.py```.

## Real World Applications

This function is a great time saver in spinning up quick classes, especially for some quick testing.
