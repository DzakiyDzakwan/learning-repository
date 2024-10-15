# Practice

## 1. Input and Variables

print(f"| ======= Body Mass Index Calculator ======== |")

"""
Write a program that asks the user for their height in centimeters and weight in kilograms. Then, calculate and print the user's Body Mass Index (BMI) using the formula:

BMI = weight / height in meters ^ 2
"""

weight = int(input("Input your weight (kg) : "))
height = int(input("Input your height (cm) : "))

height /= 100

bmi = weight / height ** 2

print(f"your body mass index is : {bmi:.2f}")

## 2. String Manipulation

print(f"\n| ======= String Manipulation Program ======== |")

"""
Question: Write a Python program that takes a full name as input and prints the following:

The name in uppercase.
The number of characters in the name (excluding spaces).
The name in reverse order.
"""

full_name = input("insert yout full_name : ")

print(f"uppercase name : {full_name.upper()}")
print(f"The number of character : {len(full_name)}")
print(f"reversed name : {full_name[::-1]}")


## 3. Check Number

print(f"\n| ======= Check Number Program ======== |")

"""
Question: Write a program that prompts the user to enter a number. The program should:

Check if the number is positive, negative, or zero.
Print an appropriate message based on the input
"""

number = int(input("input a number : "))

if number > 0 :
    print(f"the number is postive")
elif number < 0 :
    print(f"the number is negative")
else : 
    print(f"the number is zero")
    
## 4. List Loops

print(f"\n| ======= List Loops Program ======== |")

"""
Question: Create a program that asks the user to enter 5 integers, stores them in a list, and then:

Prints the list.
Prints the sum of all the numbers in the list.
Prints the largest number in the list.
"""

loop_list = []

for i in range(1,6) :
    loop_list.append(int(input(f"insert number-{i} : ")))
    
print(f"your lists : {loop_list}")
print(f"sum of the number : {sum(loop_list)}")
print(f"the largest number : {max(loop_list)}")

## 5. Patern Printing

print(f"\n| ======= List Loops Program ======== |")

"""
Question: Write a program that uses nested loops to print the following pattern:

*
* *
* * *
* * * *
* * * * *

"""


patern_height = int(input("insert the height of pattern : "))

for i in range(patern_height + 1):
    print("*"*i)
    
## Bonus Round

print(f"\n| ======= List Loops Program ======== |")

"""
Question: Write a Python program that asks the user to input a sentence and then:

Count and print the number of vowels (a, e, i, o, u) in the sentence.
"""

word_input = input("input a sentence here : ")

vowel_words = ["a", "i", "e", "o"]
vowel_number = 0

for i in word_input:
    if i in vowel_words : vowel_number += 1

print(f"number of vowel : {vowel_number}")