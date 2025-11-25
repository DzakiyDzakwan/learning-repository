"""
1. Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

Question
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
"""

expenses = [
    2200, 2350, 2600, 2130, 2190
]

# 1
answer1 = expenses[1] - expenses[0]
print(answer1)

#2
answer3 = 0
for i in range(3):
    answer3 += expenses[i]
print(answer3)

# 3
target = 2000
month = None
for i in range(len(expenses)):
    if i == target:
        month = i+1
        break

if month:
    print(f"spend $2000 on {month} month")
else:
    print(f"You never spent $200")

# Quick answer
print(2000 in expenses)

# 4
expenses.append(1980)
print(expenses)

#5
expenses[3] = expenses[3] - 200
print(expenses[3])