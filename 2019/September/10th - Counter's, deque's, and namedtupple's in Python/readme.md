# Counter's, deque's, and namedtuple's in python

Counter's, deque's, and namedtuple's are built in python datatypes as part of the collections standard library module. They each are useful in their own way, and are well worth learning.



## Counter's

Counters are a data structure used to... well count. You can add objects into the counter and you will get a tally of each object. This is most commonly used with a list of strings to tally how many occurrences of a word in text there are. Here is the code for that:



```python
from collections import Counter
import string # Used to get a list of punctuation

text = """Do not go gentle into that good night
Old age should burn and rave at close of day
Rage rage against the dying of the light

Though wise men at their end know dark is right
Because their words had forked no lightning they
Do not go gentle into that good night

Good men the last wave by crying how bright
Their frail deeds might have danced in a green bay
Rage rage against the dying of the light

Wild men who caught and sang the sun in flight
And learn too late they grieved it on its way
Do not go gentle into that good night

Grave men near death who see with blinding sight
Blind eyes could blaze like meteors and be gay
Rage rage against the dying of the light

And you my father there on the sad height
Curse bless me now with your fierce tears I pray
Do not go gentle into that good night
Rage rage against the dying of the light"""

text = text.replace("\n","").lower() # Remove newlines and set all text to lowercase
words = [] # Placeholder list to be filled with each word

for word in text.split(): # Iterate over text and add it to list
    words.append(word)

count = Counter(words) # Count occurences of strings in the list

print(count)
```



Which will print:

```python
>> Counter({'the': 11, 'of': 5, 'not': 4, 'go': 4, 'gentle': 4, 'into': 4, 'that': 4, 'good': 4, 'rage': 4, 'against': 4, 'dying': 4, 'men': 4, 'and': 3, 'at': 2, 'their': 2, 'in': 2, 'who': 2, 'on': 2, 'with': 2, 'do': 1, 'nightold': 1, 'age': 1, 'should': 1, 'burn': 1, 'rave': 1, 'close': 1, 'dayrage': 1, 'lightthough': 1, 'wise': 1, 'end': 1, 'know': 1, 'dark': 1, 'is': 1, 'rightbecause': 1, 'words': 1, 'had': 1, 'forked': 1, 'no': 1, 'lightning': 1, 'theydo': 1, 'nightgood': 1, 'last': 1, 'wave': 1, 'by': 1, 'crying': 1, 'how': 1, 'brighttheir': 1, 'frail': 1, 'deeds': 1, 'might': 1, 'have': 1, 'danced': 1, 'a': 1, 'green': 1, 'bayrage': 1, 'lightwild': 1, 'caught': 1, 'sang': 1, 'sun': 1, 'flightand': 1, 'learn': 1, 'too': 1, 'late': 1, 'they': 1, 'grieved': 1, 'it': 1, 'its': 1, 'waydo': 1, 'nightgrave': 1, 'near': 1, 'death': 1, 'see': 1, 'blinding': 1, 'sightblind': 1, 'eyes': 1, 'could': 1, 'blaze': 1, 'like': 1, 'meteors': 1, 'be': 1, 'gayrage': 1, 'lightand': 1, 'you': 1, 'my': 1, 'father': 1, 'there': 1, 'sad': 1, 'heightcurse': 1, 'bless': 1, 'me': 1, 'now': 1, 'your': 1, 'fierce': 1, 'tears': 1, 'i': 1, 'praydo': 1, 'nightrage': 1, 'light': 1})
```



## dequeu's

A collection that can be used as a queue or a stack depending on what you need. It also allows you to append to the left or right of the dequeue. An example use case could be a queueing system that keeps track of peoples position in a lineup:

```python
from collections import deque

my_queue = deque(["james","john","tommy","emilia","Candace"])

for line_location in range(len(my_queue)):
    print(f"Next in line is: {my_queue.pop()}")
```



## namedtuple's

Can be used as a psuedo-class if you want just attributes. It is used in cases where a class may have too much overhead, but you need a named collection of data or even an immutable collection of data then namedtuples are your way to go. Here is an example of a user namedtuple implementation: 

```python
from collections import namedtuple

# Create namedtuple 'Template' 
user = namedtuple("User" ,"name, age, birthday, join_date, premium")

# Allows you to specify IMMUTABLE instances in a class-like syntax
john_doe = user("John Doe", 20, "September 26th 1998", "September 9th 2019", True)

print(john_doe) # Prints: User(name='John Doe', age=20, birthday='September 26th 1998', join_date='September 9th 2019', premium=True)
```



## Demo Usage

All demo's in this repository have no dependencies and can be run using ```python <file_name>.py``` or ```python3 <file_name>.py```.



## Real World application

All of these collection types have various uses, Counters are often used in games to keep track of inventory, dequeues are used in event and theme park queuing systems to keep track of peoples places in line, and namedtuples are used all over the place for optimization.



## Additional information



 The key thing to take away from this is learning enough about these collections to use them in convenient ways. You should also take a look at the other collections available in the standard library as some of them surprised me to have a python implementation. You can find the docs for the collection module [here]( https://docs.python.org/3/library/collections.html ).