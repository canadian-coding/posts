# chr() and ord()

## Description
chr() and ord() are methods that allow you to represent integers as characters and characters as integers respectively in python. These functions rely on [ASCII numbers](http://www.asciitable.com/) to do the conversions.

## Definitions

### chr()
A built in function that takes an int (representing an ordinance/[ASCII number](http://www.asciitable.com/)) and returns a string of the corresponding single character. The inverse of the ord().function.
```python
chr(65) # Returns 'A'
chr(97) # Returns 'a'
```

### ord()
A built in function that takes a single character string and returns an int (representing its ordinance/[ASCII number](http://www.asciitable.com/)). The inverse of chr()
```python
ord("A") # Returns 65
ord("a") # Returns 97
```
### ASCII (American Standard Code for Information Interchange)
A look up table to standardize the representation of characters. For example the character 'a' is always 97 in ASCII and vice-versa. 

## Usage
In this repo you can see the demo code and actually run it by running ```python chr_and_ord.py``` or ```python3 chr_and_ord.py```.

## Real World Applications
The real world applications for these functions are usually very specific. Sometimes they are used to handle low-level character compatibility layers for legacy systems. But one simpler usage that i've run into, is for working with xlsx files. 

xlsx files are the default Microsoft Excel extension files, in these files workbooks are ordered by row (numbers) and columns (letters). So to iterate through a set of rows you would need 'column_letter row_number' for example: "A1" --> "A2" --> "A3" etc. For rows you can iterate using ints, but for columns since they are individual characters to iterate you can convert them using ord and then increment/decrement and convert back to the correct character with chr.

For example:
```python
import xlsxwriter # Third part module for working with xlsx files

filename = "data.xlsx"

workbook = xlsxwriter.Workbook(filename) # Create new workbook for data.xlsx
worksheet = workbook.add_worksheet() # Add a worksheet to put data into

data = [1,2,3,4] # list to iterate over

column = ord("A") # Initializing column counter: in this case 65

for number in data:
    worksheet.write("{}1".format(chr(column)), data[number]) # Writes data to A1, then B1, then C1 etc.
    column += 1

workbook.close() # Close workbook file and write data
```