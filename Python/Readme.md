# Python Learning Path

This folder contains materials for learning python

## Learning Content :

- How to install python
- How to run python program
- Basic python
  - Introduction
  - Compiling Program
  - Variables
  - Data Type
  - Type Annotation
  - Data Type Casting
  - Input
  - Operation

## How to Install Python

1. Go to [https://python.org](https://python.org)
2. Go to download, then click the latest version of Python
3. Then run the installation setup, check all the checkbox on the first page then click install now
4. To check if python installed, run `python --version` on terminal

## How to Run Python Program

1. To run a python program you can run this command

```
python <file_name>.py
```

## Basic Python

Python is an interpreter programming language. You can run python program without executable file like C++, Java and Go.

### Introduction

Using print() to print a data

```
print(hello World)
print(56)
print(true)
```

Python doesn't need `;` to end an expression

To run a python program run command `python <file_name>.py`

#### Comment

1. Singleline comment

```
# this is a single line comment for python
```

2. Multiline comment

```
"""
This is a multi line comment
"""
```

### Compiling program

Although python is an interpreter language, python programs can also be compiled to reduce runtime execution. To compile a python program you can use `python -m py_compile <file_name>.py`. It's going to create a new folder called `__pycache__` to save the output of compilation. Run the compiled program using `python __pycache__/<compiled_name>.pyc`.

To check a excecution runtime you can use

```
import time
start_time = time.time();

print(time.time() - start_time, "detik")
```

### Variables

to declare a variable in python. You just need to declare varible name and assign the value

```
name = "Dzakiy Dzakwan"
age = 22
is_good = False
```

### Data Type

Same like any other programming language the difference is in python you dont need declare the data type like in java or C. Here are the function to check what type is the variable

```
type(variable)
```

1. String

```
string_data = "this is string"
print("data : ", string_data, "type : ", type(string_data))
```

2. Integer

```
int_data = 79
print("data : ", int_data, "type : ", type(int_data))
```

3. Float

```
float_data = 3.5
print("data : ", float_data, "type : ", type(float_data))
```

4. Boolean

```
bool_data = True
print("data : ", bool_data, "type : ", type(bool_data))

bool_data_2 = False
print("data : ", bool_data_2, "type : ", type(bool_data_2))
```

4. Complex

```
complex_data = complex(5, 1)
print("data : ", complex_data, "type : ", type(complex_data))
```

5. C language data type
   In python you can use C language data type like char, float, double, etc...

Example :

```
from ctypes import c_double

double_data = c_double(3.14)
print("data : ", double_data, "type : ", type(double_data))
```

### Type Annotation

In pyhton you can declare variable with type annotation to specify the expected data type of variables, function, arguments, and return value.

```
name: str = "Dzakiy Dzakwan"
age: int = 22
is_student: bool = True
```

### Data Type Casting

```
# Example here is a data with float data type
float_data_2 = 7.5

# Change data to string, integer and boolean
string_data_cast = str(float_data_2)
integer_data_cast = int(float_data_2) # Integer will floor round, the value will become 7
bool_data_cast = bool(float_data_2)
```

### Input

To get input from user you can use `input()`, every input stored as string data. If you want use input data for another data type, you need to cast the string type into anothe type. Example :

```
is_married = input("have you ever been married ? [1 = yes, 0 = no]")
is_married = bool(int(is_married))

print(is_married)
```

### Operators

1. Aritmethic Operation

```
a = 6
b = 2

print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a % b) # Modulo
print(a ** b) # Exponentiation
print(a // b) # Floor Division
```

2. Comparison Operator

```
a = 2
b = 3

print(a, ">", b, "=", a > b) # Greater than
print(a, "<", b, "=", a < b) # Less than
print(a, ">=", b, "=", a >= b) # Greater than or Equal to
print(a, "<=", b, "=", a <= b) # Less than or Equal to
print(a, "==", b, "=", a == b) # Equal to
print(a, "!=", b, "=", a != b) # Not Equal to
```

3. Object Identity Operator

this operator is used to compare the identity of two objects, i.e., whether they refer to the same memory location.

```
c = 5
d = 5
e = d


print("c = ", c, " id = ", hex(c))
print("d = ", d, " id = ", hex(d))

print("c is d = ", c is d)
print("c is not d = ", c is not d)
```

`c` and `d` is the same object in memory
`c` and `e` or `d` and `e` is not the same object altough they have same value

4. Logical Operator

```
x = True
y = False

print("X and Y = ", x and y) # And Operator
print("X or Y", x or y) # Or Operator
print("Negation X and Y = ", not(x and y))

```

5. Bitwise Operator

   Bitwise operators are used to perform bit-level operations on integers. These operators treat the numbers as a sequence of bits (binary representation) and perform operations directly on these bits.

   - AND Operator `&`
     Sets each bit to 1 if both bits are 1

   - OR Operator `|`
     Sets each bit to 1 if one of two bits is 1

   - XOR Operator `^`
     Sets each bit to 1 if only one of two bits is 1

   - NOT Operator `~`
     Inverts all the bits

   - Zero Fill Left Shift
     Shift left by pushing zeros in from the right and let the leftmost bits fall off

   - Signed Right Shift
     Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

6. Assignment Operator

- `x += 3`, is equal to `x = x + 3`
- `x -= 3`, is equal to `x = x - 3`
- `x *= 3`, is equal to `x = x * 3`
- `x /= 3`, is equal to `x = x / 3`

Assignment operator also can be applied with bitwise operator

- `x &= 3`, is equal to `x = x & 3`
- `x |= 3`, is equal to `x = x | 3`
- `x ^= 3`, is equal to `x = x ^ 3`

### String

1. Create a String
   To Create a String you can use `'` and `"`. But you can make multiline string using `"""`

   ```
   kalimat_1 = 'this is a string with single quote'

   kalimat_2 = 'this is a string with double quote'

   kalimat_3 = """
      Here is
      a multiline
      string
   """
   ```

2. Backlash Character

- `\'` Single Quote
- `\"` Double Quote
- `\n` New Line
- `\t` Tab
- `\b` Backspace
- `\\` Backslash

If you want to make Backslash as string character you can use raw string

```
kalimat = r"D:\Application\Projects\Python"
```

3. String Manipulation

- Check if there is character or string inside another string

```
string = "Hello World"
print("Hello" in string)
```

- Check if there is no character or string inside another string

```
string = "Hello World"
print("Hello" not in string)
```

- Repeat a String

```
string = "wk"*5 # Result wkwkwkwkwk
```

- indexing

```
string = "abcde"

# taking character from front
print(string[0]) # a
print(string[1]) # b

# taking character from behind
print(string[-1]) # e
print(string[-2]) # d

# taking character from index 0 - 3
print(string[0:3]) # abc
```

- Min and Max

Min and Max on string is used to take a lowest ascii number (min) and highest ascii number (max) for character in a string

```
string = "abclmnxyz"

max(string) # z, is the highest
min(string) # a, is the lowest
```

- Count

Count is used to count how many character or word on a string

```
string = "abada"

print(string.count("a")) # There is 3 a in string

```

- Lower and Upper
  lower() and upper() is a method to change a string into lowercase or uppercase

```
string = "Sigma"

print(string.lower()) # the result become, sigma
print(string.upper()) # the result become, SIGMA
```

to check if a string is an uppercase or lowercase you can use `islower()` and `isupper()`

another method are

1. `isalpha()`,to check a string only contains alphabet
2. `isalnum()`, to check a string contains alphabet and number
3. `isdecimal()`, to check a string only contains number
4. `isspace()`, to check a string contains space, tab, newline
5. `istitle()`, to check a string start with capital word

- Allocation String

1. `rjust()`
2. `ljust()`
3. `center()`

4. Format String a.k.a String Literal
   you can use f before `f""` like this to create a format string, it's the same like raw string `r""`

```
nama = "Dzakiy"
print(f"Halo selamat datang {nama}")
```

You can show float number, showing negative or positve and percentage

```
float_number = 10.0754
print(f"Decimal Number : {float_number:.2f}") # 2 number behind coma
print(f"Decimal Number : {float_number:.1f}") # 1 number behind coma
```

```
positive_number = +10
negative_number = -5

print(f"positive number : {positive_number:+}")
print(f"negative number : {negative_number:+d}")
```

```
percentage_number = 0.10
print(f"persentase : {percentage_number:%}")
```

5. Number System

You can change number system from octal into binary or hexadecimal

```
angka = 10

binary = bin(angka)
octal = oct(angka)
hexadecimal = hex(angka)

print(binary)
print(octal)
print(hexadecimal)
```

6. Date and Time

To manipulate date and time you need a package called datetime, the first thing you need is to import the package

```
import datetime as dt
```

- Get time now

```
now = dt.datetime.now()
```

- Get today

```
today - dt.date.today()
```

- Create Custom Date

```
custom_date = dt.date(year, month, day)
```

- String Format Time

```
today = dt.date.now()

today.strftime("%Y") # get year
today.strftime("%B") # get month
today.strftime("%d") # get day
today.strftime("%A") # get weekday
```

or you can use string format like this

```
print(f"Today {today:%A}, {today.day} {today:%B} {today:%Y}")
```

### Conditions Statement

```
if <condition> :
  <action>
elif <condition2> :
  <action 2>
else
  <else action>
```

example :

```
a = 5
b = 6

if(a > b) :
  print(f"{a} is higher then {b}")
else :
  print(f"{a} is lower then {b}")
```

in python there is no curly bracket `{}` in if statement. So to make a difference between if statement to next line is with identation. And if you only have 1 action to do in each statement you can create if statement in 1 line. This only work for if else statement and not working for i elif else statement

```
<action> if <condition> else <else_condition>
```

you can use pass to pass the action in statement like this

```
if 1 > 5 :
  pass
elif 1 = 5:
  print("congratulation")
else:
  print("too bad")
```

### For Statement

1. For Loop

```
for i in range(10) :
    print(f"index-{i}")
```

Looping with list

```
numbers = [2, 4, 6, 8, 10]

for i in numbers:
    print(f"number-{i}")

number = 10
```

2. While Loop

```
while(number > 0) :
    print(number)
    number -= 1

number = 1
```

### Break, Pass and Continue

1. `break` will exit loop entirely

```
for i in range(5)
  if i / 5 == 0 :
    break # it will break the loop if i is 5
```

2. `pass` will does nothing, act as a placeholder

```
for i in range(5)
  if i / 5 == 0 :
    pass # it will does nothing if i is 5
```

3. `continue` will skips the rest of the current iteration and proceeds to the next

```
for i in range(5)
  if i / 5 == 0 :
    continue # it will continue to the next iteration without executing below code

  print("this text will not showing if i is 5")
```

### List

List is 1 of 4 collection data type from python. List is like an array in another programming language

```
numbers = [1, 2, 3, 4, 5, 6]

strings = ['ucup', 'otong', 'odin']

booleans = [True, False, True, True]

mixes = [1, "ucup", True, "udin", False]
```

or you can create list with list() like this

```
array = list([1,2,3,4,5])
```

alternative way to create list is using loop or range

```
list_range = list(range(1, 11, 1)) # range (start, stop, step)
```

```
list_for = [i*2 for i in range(1, 6)] #[1, 4, 6, 8, 10 ]
```

you can add if to in for loop list

```
list_for_if = [i**2 for i in range(1, 6) if i % 2 != 1 ] #[4, 16]
```

same like string you can acess list value using index

```
list = ["a", "b", "c", "d", "e"]
print(list[0]) # get the first value of array (a)
print(list[-1]) # get the last value of array (e)
```

#### List Manipulation

1. len()

return the length of array

```
list = ["a", "b", "c", "d", "e"]

print(len(list)) # the lenght of array is 5
```

2. insert()
   adding a new data to the list with selected position

```
list = ["a", "b", "c", "d", "e"]

list.insert(1, 'f') # ["a", "f", "b", "c", "d", "e"]
```

3. append()
   adding a new data to the list on the last position

```
list = ["a", "b", "c", "d", "e"]

list.append('f') # ["a", "b", "c", "d", "e", "f"]
```

4. extend()
   extend list with another list

```
list = ["a", "b", "c", "d", "e"]
list2 = ["f", "g"]

list.extend(list2) # ["a", "b", "c", "d", "e", "f", "g"]
```

5. remove()
   to remove selected data

```
list = ["a", "b", "c", "d", "e"]

list.remove("c") # ["a", "b", "d", "e"]
```

6. sort()
   to sort list data value

```
list = ["e", "d", "a", "b", "e"]

list.sort() # ["a", "b", "c", "d", "e"]
```

7. reverse()
   to reverse data in list

```
list = ["a", "b", "c", "d", "e"]

list.reverse() # ["e", "d", "c", "b", "a"]
```

8. enumerate()

enumarate are a method you can use to get index and value of a list

```
list = ["a", "b", "c", "d", "e"]

for index, item in enumerate(list) :
  print(f"{index}- {item}")
```

#### Copy List

To copy a list in python you cant do like this

```
a = ["a", "b", "c", "d", "e"]
b = a

# if i change a value from list b

b[1] = "f"

this will change both of list a and list b

a = ["a", "f", "c", "d", "e"]
b = ["a", "f", "c", "d", "e"]
```

this case happen because data from list b and list a has the same memory address. So to copy a list you need to use `copy` method like this

```
a = ["a", "b", "c", "d", "e"]

b = a.copy()

b[1] = "f"

a = ["a", "b", "c", "d", "e"]
b = ["a", "f", "c", "d", "e"]
```

`copy` method will make a new array with the same value and difference memory address

#### Nested List / Multi Dimensional List

```
list_2d = ["a", "f", "c", "d", "e"]
list_3d = [["a", 1], ["b", 2], ["c", 3], ["d", 4], ["e", 5]]
```

In Multidimensional List you cant use copy() method to copy a list, Because it will only copy the first dimension list. But the second dimension it will not change the memory address

```
a = [["a", 1], ["b", 2], ["c", 3], ["d", 4], ["e", 5]]
b = a.copy()

b[0][1] = [3]

a = [["a", 3], ["b", 2], ["c", 3], ["d", 4], ["e", 5]]
b = [["a", 3], ["b", 2], ["c", 3], ["d", 4], ["e", 5]]
```

You need a deepcopy method from copy package to copy a multidimensional list

```
from copy import deepcopy

a = [["a", 1], ["b", 2], ["c", 3], ["d", 4], ["e", 5]]
b = deepcopy(a)

b[0][1] = [3]

a = [["a", 1], ["b", 2], ["c", 3], ["d", 4], ["e", 5]]
b = [["a", 3], ["b", 2], ["c", 3], ["d", 4], ["e", 5]]
```

### Tuple

Tuple is 2 of 4 collection data type from python. Tuple is immutable, that means the value in tuples cant be change. Or the easy explanation tuple is constant collection

```
tuples = ("udin", "mulyono", "jono")

tuples2 = tuple("udin", "mulyono", "jono")
```

Like a list, tupple can be acessed using index

```
tuples = ("udin", "mulyono", "jono")

print(tuples[1]) # mulyono
```

tuple can contains different data type like list

### Set

Set is 3 of 4 collection data type from python, set is unordered and no indexable. Set is usefull if you want to have a unique collection.

```
sets = {1, 3, 5, 7, 9}

sets2 = set(1, 3, 5, 7, 9)
```

set cannot accessed using index like list and tuple

### Dictionary

Dictionary is 4 of 4 collection data type from python, dictionary store data in key-value pairs. Dictionary is like object data type from javascript

```
dictionaries = {
  key : value,
  key2 : value2
}
```

to access data from the dictionary you can call the key as an index like this

```
dictionaries = {
  "key" : "value",
  "key2" : "value2"
}

print(dictionaries['key2']) # it return value 2
```

or you can use get method to get the value from dictionary. the difference between using index key and get method is with using get you can handle the error like this

```
dictionaries = {
  "key" : "value",
  "key2" : "value2"
}

dictionaries.get('key3', 'key not found') # if key with name key3 not found then it will return 'key not found'
```

to update dictionary data dictionary has a method called update, update will update an existing key or if the key not exist it will add new key to the dictionary

```
dictionaries = {
  "key" : "value",
  "key2" : "value2"
}

dictionaries.update({"key3" : "value3"}) # it will add new key-value pair to dictionary cause 'key3' is not exists
```

to delete data in dictionary you can use this

```
dictionaries = {
  "key" : "value",
  "key2" : "value2",
  "key3" : "value3"
}

del dictionaries["key3"] # it will remove "key3" from dictionaries
```

or you can use `pop()` method to remove a key data from dictionary. You can transfer remove data to another variable like this

```
dictionaries = {
  "key" : "value",
  "key2" : "value2",
  "key3" : "value3"
}

new_key2 = dictionaries.pop('key2') # it will remove key 2 from dictionaries but it will save the value of key2 into new_key2
```

last, the same like list you can copy a dictionary using `copy()` method to make a difference memory address

```
dictionaries = {
  "key" : "value",
  "key2" : "value2",
  "key3" : "value3"
}

new_dictionaries = dictionaries.copy()

```

#### Dictionary Loop

1. keys()

`keys()` is a method to get iterable colection of key from dictionary

```
person = {
  "name" : "Dzakiy"
  "age" : 12
  "address" : "Surabaya"
}

keys = person.keys()

for key in keys
  print(key) # it will return all key data
```

2. values()

`values()` is a method to get iterable collection of value from dictionary

```
person = {
  "name" : "Dzakiy"
  "age" : 12
  "address" : "Surabaya"
}

values = person.values()

for value in values
  print(value) # it will return all key data
```

3. items()

`items()` is a method to get iterable collection of key and value from dictionary

```
person = {
  "name" : "Dzakiy"
  "age" : 12
  "address" : "Surabaya"
}

items = person.items()

for key, value in items
  print(key, value) # it will return all key, value of data
```

#### Nested Dictionary

```
persons = {
    "P001" : {
      "name" : "Dzakiy"
      "age" : 12
      "address" : "Surabaya"
    },
    "P002" : {
      "name" : "Dzakwan"
      "age" : 24
      "address" : "Medan"
    },
}
```

### Function

```
def <function_name>(argument) :
  # expression here
```

example

```
def greet_parameter(name: str) :
    print(f"Hello {name} welcome to function course")
```

example of function with many returns

```
## Function with many return

def operator(number1:int, number2:int) :
    adition = number1 + number2
    subtraction = number1 - number2
    multiply = number1 * number2

    return adition, subtraction, multiply

adition, subtraction, multiply = operator(1, 2)

print(adition) # 3
print(subtraction) # -1
print(multiply) # 2
```

#### \*args

`*args` is a way to change an arguments into a tuple inside the function. Example

```
def sumarize(*numbers) :
    total = 0
    for number in numbers :
        total += number

    return total

print(sumarize(1,3,5,7,9)) # return 25
print(sumarize(2,4,6,8,10)) # return 30
```

#### `**kwargs`

`**kwargs` is a keyword argument, this is a way to change an argument into a dictionary. You need to set a keyword when you want insert an argument

```
def getMember(**member) :
    print(f"welcome {member['name']}, you have been joined this club since {member['year']}")

getMember(name = "Dzakiy", year = 2008)
```

### lambda

lambda is a way to create small, anonymous (unnamed) functions. Unlike regular functions defined using def, a lambda function can have any number of arguments but only one expression. The expression is evaluated and returned.

```
power = lambda parameter: <expression>
```

Contoh penggunaaan

```
numbers = [1,2,4,5,9,10]

def is_even(number):
  return angka % 2 == 0

new_numbers = list(filter(is_even, numbers))
```

it would be shorter if you using lambda

```
numbers = [1,2,4,5,9,10]

new_numbers = list(filter(lambda number: angka % 2 == 0, numbers))
```

Or you can make anonymous function inside another function

```
def myFunction(n) :
    return lambda a : a ** n

doubleFunction = myFunction(2)
tripleFunction = myFunction(3)

print(doubleFunction(4))
print(tripleFunction(4))
```

### Module

Module is a self-contained file containing Python definitions and statements. It's like a toolbox, organized to hold specific functions, classes, and variables.

- Import Statement

```
import <module_name>
```

- Import Specific Parts Statement

```
from <module_name> import <specific_function>, <specific_class>
```

- Add Alliases

```
import <module_name> as <aliases_name>
```

## Python GUI

Graphical User Interface (GUI) in Python allows you to create visually appealing and user-friendly applications.

There is several toolkits to Build GUI

- Tkinter
- PyQt
- wxPython
- Kivy

Example of build GUI application wiht python

```
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()

# Configure Window
window.configure(bg='white')

# Window frame Size
window.geometry("800x500")

# Disabled window resizable
window.resizable(False, False)

# Window Title
window.title('Test Application')

# Adding Frame
frame_1 = ttk.Frame(window)

## Grid Pack Placement
frame_1.pack(padx=24, pady=24, fill="x")

# Other Component
FIRST_NAME = tk.StringVar()

label_fname = ttk.Label(frame_1, text="First Name")
label_fname.pack()

input_fname = ttk.Entry(frame_1, textvariable=FIRST_NAME)
input_fname.pack()

LAST_NAME = tk.StringVar()
label_lname = ttk.Label(frame_1, text="Last Name")
label_lname.pack()

input_lname = ttk.Entry(frame_1, textvariable=LAST_NAME)
input_lname.pack()

def handleSubmit():
    """
    This function will called after the button got clicked by User
    """
    message = f"Congrats {FIRST_NAME.get()} {LAST_NAME.get()} you have clicked the button"
    messagebox.showinfo("New Message", message)

button_submit = ttk.Button(frame_1, text='Submit', command=handleSubmit)
button_submit.pack(pady=12)

# Window lopp so it doesn't close
window.mainloop()
```
