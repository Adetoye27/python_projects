#write a program that will ask for a user body weight in pound (lbs) and convert it to kilogram(kg)
#Display on the screen, Your body weight in lbs and the equivalent in kgs is weight kg
#only display 3 decimal digit

#Input your weight

weight = float(input("What is your body weight in lbs:  "))
new_weight_kg = weight * 0.453592

#print the output
print(f"Your body weight is: {weight} in lbs and the equivalent in kgs is: {new_weight_kg:.3f} kg")