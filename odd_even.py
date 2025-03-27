# Write a program that will ask a user for a number 
# then check whether that number is EVEN or ODD
# Display on the screen:
# Please enter a number between 1 and 100
# Your number user_number is even/odd

user_number = int(input("Please enter a number between 1 and 100:\n"))

if 1 <= user_number <= 100:
    if user_number % 2 == 0:
        print(f"Your number {user_number} is even")
    else:
        print(f"Your number {user_number} is odd")
else:
    print(f"ERROR: Your number {user_number} is out of range")

# Ensuring a newline at the end of the file
