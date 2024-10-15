# Write a Python program that uses a list of four U.S. women athletes who have competed in the 400 meters at the Olympics. Your program should do the following:
# Create a list called athletes with the following names:
# Allyson Felix
# Sanya Richards-Ross
# Shaunae Miller-Uibo
# Phyllis Francis
# Use a for loop to display each athlete's name along with the lap number they completed. The output should be in the following format:

athletes = ["Allyson Felix","Sanya Richards-Ross", "Shaunae Miller-Uibo", "Phyllis Francis"]

for index in range(len(athletes)):
    print(f"Lap {index + 1}: {athletes[index] } has completed their lap!")
print("All athletes have completed their laps!")