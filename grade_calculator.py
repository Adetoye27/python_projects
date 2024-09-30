#write a program that will ask  a student for grade in 5 subjects
#calculate the average grade  and print  grade A-E

grade1 = float(input("What's your grade in the 1st Subject: "))
grade2 = float(input("What's your grade in the 2nd Subject: "))
grade3 = float(input("What's your grade in the 3rd Subject: "))
grade4 = float(input("What's your grade in the 4th Subject: "))
grade5 = float(input("What's your grade in the 5th Subject: "))

average = (grade1 + grade2 + grade3 + grade4 + grade5) / 5

if average > 90:
    print("A")
elif average > 80 and average < 90:
    print("B")
elif average > 70 and average < 80:
    print("C")
elif average > 60 and average < 70:
    print("D")
else:
    print("You FAILED!!! BETTER LUCK NEXT TIME")