#python program displaying custom banner for the streetfighter game

#declared variables
spec_char = "#"
name = "Adetoye"
prompt = "WELCOME TO STREET FIGHTER:  "

first_line = spec_char * 41
second_line = f"{spec_char}\t\t\t\t\t{spec_char}"
third_line = spec_char + " " + prompt + name + '\t' + spec_char
fourth_line = f"{spec_char}\t\t\t\t\t{spec_char}"
fifth_line = spec_char * 41

print(f"{first_line}\n{second_line}\n{third_line}\n{fourth_line}\n{fifth_line}")