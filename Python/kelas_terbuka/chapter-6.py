# Tuples
tupples = ("Joni", "Jono", "Jontor")
tupples2= tuple({1, 2, 3, 4})

print(tupples)
print(type(tupples))



# Sets
sets = {1, 5, 9, 11}
sets2 = set({1, 2, 3, 4, 5})

print(sets)
print(type(sets))

# print(sets[1]) 
#can not acessed set value with index 1, because set not indexable


# Dictionary

person1 = {
    "name" : "Dzakiy",
    "age" : 12,
    "address" : "Surabaya"
}

person2 = {
    "name" : "Dzakwan",
    "age" : 24,
    "address" : "Medan" 
}

persons = {
    "P001" : person1,
    "P002" : person2
}

print(persons)
print(f"persons 1 : {persons.get("P001")}")
print(f"persons 2 : {persons.get("P002")}")

# 1st
for key in persons.keys():
    print(f"{persons[key]["name"]:>5} {persons[key]["age"]}")
   
# 2nd 
for person in persons.values():
    print(f"{person["name"]:>5} {person["age"]}")
    
# 3rd

for key, person in persons.items():
    print(f"{key} : {person["name"]:>5} {person["age"]}")