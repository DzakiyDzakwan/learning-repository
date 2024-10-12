# LIST

numbers = [1, 2, 3, 4, 5, 6]
strings = ['ucup', 'otong', 'odin']
booleans = [True, False, True, True]
mixes = [1, "ucup", True, "udin", False]

print(numbers)
print(strings)
print(booleans)
print(mixes)


## Alternative way to create list

data_range = range(1, 11, 1) # start, stop, step
number_range = list(data_range)

print(number_range)

list_for = [i*2 for i in range(1, 6)]
list_for_if = [i**2 for i in range(1, 6) if i % 2 != 1 ]

print(list_for)
print(list_for_if)

## List Manipulation

list = ["a", "b", "c", "d", "e"]

print(len(list))
list.insert(1, 'f')
list.append('f') 

print(list)
list.remove('f')

list_2 = ["f", "g"]
list.extend(list_2)
print(list)

list.reverse()
print(list)

a = ["a", "b", "c", "d", "e"]
b = a.copy()

b[1] = "f"

print(a, b)

from copy import deepcopy
c = [["a", 1], ["b", 2], ["c", 3], ["d", 4], ["e", 5]]
d = deepcopy(c)

d[0][1] = 3

print(c)
print(d)
