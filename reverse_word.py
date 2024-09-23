#write a program that will ask for a word and reverse the word
#display on the screen your word is:word and the reverse is reverse_word

#ask user for a word
word = input("What word do you want reversed:\n")

#Using the reversed method to reverse the word
reverse_word = ''.join(reversed(word))

#Print the output
print(f"Your word is: {word} and the reverse is {reverse_word}")