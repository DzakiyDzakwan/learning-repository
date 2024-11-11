import random
# import  my_module

random_number = random.randint(1, 10)

# print(random_number)
# print(my_module.my_name)

# random_float = random.random() * 10
random_float = random.uniform(0, 10)
print(random_float)

# Head and Tail

is_head = random.randint(0,1)
print('Head')  if is_head == 1 else print("Tail")

