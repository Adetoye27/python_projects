#write a program  that will ask a user for a number then check whether that number is EVEN or odd
#Display on the screen:
#Please enter a number between 1 and 100
#Your number user_number is even/odd

user_number = int(input("Please enter a number betwwn 1 and 100 \n"))

if (user_number >= 1 and user_number <= 100) and (user_number % 2 ==0 ):
    print(f"Your number {user_number} is even")
elif (user_number >= 1 and user_number <= 100) and (user_number % 2 != 0):
    print(f"Your number {user_number} is odd")
else:
    print(f"ERROR: Your number {user_number} is out of range")