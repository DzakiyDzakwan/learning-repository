# String

## Backslash
kata1 = "i\'m a student"
print(kata1)

kata2 = 'He said \"Good morning all\"'
print(kata2)

kata3 = "\n Here is a new line"
print(kata3)

kata4 = "\t There will be tab indent"
print(kata4)

## Raw String

raw_string = r"Here is a raw string for '\' character"
print(raw_string)

## Multiline String

print(""" 
Here is
a multiline
string
""")

## String Manipulation

string = "Hello World"
print("Hello" in string) # use in to check if string or char exists in targeted string
print("Hello" in string) # use not in to check if string or char doesnt exists in targeted string


## Indexing

string = "abcde"

print(string[0])
print(string[1])

print(string[-1])
print(string[-2])

print(string[0:3])

## Min Max

string = "abcklmxyz"
print(min(string))
print(max(string))

## Count

string = "abcde"

print(string.count("a")) # There is 1 a in string

## lower and upper

string = "Sigma"

print(string.lower()) # the result become, sigma
print(string.upper()) # the result become, SIGMA

## Format String a.k.a String Literal

nama = "Dzakiy"
print(f"Halo selamat datang {nama}")

### Show float number
float_number = 10.0754
print(f"Decimal Number : {float_number:.2f}") # 2 number behind coma
print(f"Decimal Number : {float_number:.1f}") # 1 number behind coma

### Show + or -
positive_number = +10
negative_number = -5

print(f"positive number : {positive_number:+}")
print(f"negative number : {negative_number:+d}")

### Percentage
percentage_number = 0.10

print(f"persentase : {percentage_number:%}")


## Format Angka Lainnya

angka = 10

binary = bin(angka)
octal = oct(angka)
hexadecimal = hex(angka)

print(binary)
print(octal)
print(hexadecimal)

## Date and Time
import datetime as dt

### Get now time
this_time = dt.datetime.now()

print(f"waktu saat ini adalah {this_time}")

### Get today date
today = dt.date.today()

print(f"tanggal hari ini adalah {today}")
print(f"hari ini adalah {today:%A}")
print(f"bulan hari ini adalah {today:%B}")
print(f"tahun hari ini adalah {today:%Y}")


### Create a Date
new_date = dt.date(2002, 12, 1)

print(f"tanggal kemarin adalah {new_date}")
print(f"hari kemarin adalah {new_date:%A}")
print(f"bulan hari kemarin adalah {new_date:%B}")
print(f"tahun hari kemarin adalah {new_date:%Y}")