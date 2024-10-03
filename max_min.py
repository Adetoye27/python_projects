#write a python program that prints the largest and smallest values in a list
#print the 2 values values on the same line, seperated by space
#The largest value should appear before the smallest value 
#You  may assume that the list only contains numeric values
# If the list is empty, print None

number1 = input("what is the number here: ")
number2 = input("what is the number here: ")
number3 = input("what is the number here: ")
number4 = input("what is the number here: ")

numbers = []
if number1:
    numbers.append(int(number1))
if number2:
    numbers.append(int(number2))
if number3:
    numbers.append(int(number3))
if number4:
    numbers.append(int(number4))


if not numbers:
    print((numbers))
else:
    print(numbers)
    print(f"The largest and the smallest value  of the list are: \n {max(numbers)} {min(numbers)} ")








