# Python Learning Path

This folder contains materials for learning python

## Learning Content :

- How to install python
- How to run python program
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
