# Operator

## Arithmetic Operator

a = 6
b = 2

print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a % b) # Modulo
print(a ** b) # Exponentiation
print(a // b) # Floor Division

## Comparison Operator

print(a, ">", b, "=", a > b) # Greater than
print(a, "<", b, "=", a < b) # Less than
print(a, ">=", b, "=", a >= b) # Greater than or Equal to
print(a, "<=", b, "=", a <= b) # Less than or Equal to
print(a, "==", b, "=", a == b) # Equal to
print(a, "!=", b, "=", a != b) # Not Equal to

## Object Identity Operator
c = 5
d = 5


print("c = ", c, " id = ", hex(c))
print("d = ", d, " id = ", hex(d))

print("c is d = ", c is d)
print("c is not d = ", c is not d)

## Logical Operator

x = True
y = False

print("X and Y = ", x and y) # And Operator
print("X or Y", x or y) # Or Operator
print("Negation X and Y = ", not(x and y))


## Bitwise Operator

### AND Operator
print("A = ", format(a, "08b"))
print("B = ", format(b, "08b"))
print("------------------ AND")

c = a & b
print("C = ", format(c, "08b"))


### OR Operator
print("A = ", format(a, "08b"))
print("B = ", format(b, "08b"))
print("------------------ OR")

c = a | b
print("C = ", format(c, "08b"))

### XOR Operator
print("A = ", format(a, "08b"))
print("B = ", format(b, "08b"))
print("------------------ XOR")

c = a ^ b
print("C = ", format(c, "08b"))

### NOT Operator
print("A = ", format(a, "08b"))
print("Not A = ", format(~a, "08b"))

### Zero Fill Left Shift
print("A = ", format(a, "08b"))
print("Zero Fill Left Shift A = ", format(a << 1, "08b"))

### Zero Fill Right Shift
print("A = ", format(a, "08b"))
print("Zero Fill Right Shift A = ", format(a >> 1, "08b"))