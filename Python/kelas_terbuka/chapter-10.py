# Reading File

print(10*"=", "Read File" ,10*"=")
file = open("text.txt", mode="r")

## Check if file is readable
print(f"is readable : {file.readable()}")


# print(file.read())

# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())

# Write File

## Check if file is writeable
print(f"is writable : {file.writable()}")

# Close File

file.close()