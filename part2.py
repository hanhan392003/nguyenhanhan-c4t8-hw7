numbers = [0, 2, 5, 7, 9, 11]

# ex 7
number = int(input("Enter a number: "))
if number not in numbers:
    print("Not found in the list")
else:
    print("Found, position:", numbers.index(number)+1)

# ex 8
sum = 0
for i in numbers:
    sum += i
print("Sum of all numbers:", sum)

# ex 9
new_numbers = input("Enter the numbers: ")
new_numbers_sum = 0
new_numbers_split = new_numbers.split(" ")
for new_number in new_numbers_split:
    new_number = int(new_number)
    new_numbers_sum += new_number
print("Sum of all numbers:", new_numbers_sum)

# ex 10
even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
print("Even number(s):", *even_numbers)

# ex 11
new_numbers_list = input("Enter the numbers: ")
new_even_numbers = []
new_numbers_list_split = new_numbers_list.split(",")
print(new_numbers_list_split)
for new_item in new_numbers_list_split:
    new_item = int(new_item)
    if new_item % 2 == 0:
        new_even_numbers.append(new_item)
# print(new_even_numbers)
print("even numbers:", *new_even_numbers)