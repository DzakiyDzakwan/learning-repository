# Variables

name = "Dzakiy Dzakwan"
age = 22
is_good = False

# Data Type 

## String
string_data = "this is string"
print("data : ", string_data, "type : ", type(string_data))

## Integer
int_data = 79
print("data : ", int_data, "type : ", type(int_data))

## Float
float_data = 3.5
print("data : ", float_data, "type : ", type(float_data))

## Biner/Boolean
bool_data = True
print("data : ", bool_data, "type : ", type(bool_data))

bool_data_2 = False
print("data : ", bool_data_2, "type : ", type(bool_data_2))

## Complex
complex_data = complex(5, 1)
print("data : ", complex_data, "type : ", type(complex_data))

## C language data type
### C Boolean
from ctypes import c_double

double_data = c_double(3.14)
print("data : ", double_data, "type : ", type(double_data))

### C Float
from ctypes import c_float

float_data = c_float(1.2)
print("data : ", float_data, "type : ", type(float_data))

## Data Type Casting
float_data_2 = 7.5

string_data_cast = str(float_data_2)
integer_data_cast = int(float_data_2) # The value will become 7
bool_data_cast = bool(float_data_2)