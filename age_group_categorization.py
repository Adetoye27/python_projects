# Prompt the user to enter their age as an integer
#Based on the input, categorize the person into one of the following 
# Infant (0-1), Toddler (2-3), child (4-12), Teenager (13-19), Adult (20-64), Senior (65 or older)

age = int(input("what is your age today: "))

if age >= 0 and age <= 1:
    print("You are an Infant")
elif age >=2 and age <=3 :
    print("You are a Toddler")
elif age >=4 and age <=12 :
    print("You are a Child")
elif age >= 13 and age <= 19 :
    print("You are a Teenager")
elif age >=20 and age <= 64 :
    print("You are a Adult")
elif age >= 65 and age <= 150:
    print("You are a Senior")
else:
    print("ERROR: The age is invalid")