# Practice reversing a list and transferring its elements into a new list using loops.
# Task: Write a Python program that works with the list called laura_things containing the following items:
# "sewing machine"
# "scissor"
# "cutting mat"
# "television"



laura_things = ["sewing machine", "scissor", "cutting mat", "television"] 
reversed_things = []
for i in laura_things:
    reversed_things.append(i)
reversed_things = reversed_things[::-1]
print(f"The reversed list is: {reversed_things}")
print("The list has been successfully reversed!")