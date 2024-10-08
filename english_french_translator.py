#create an english french translator program. The program takes a word from the user as an input
#and translate it using the dictionary data type as vocabulary
#Please add the translation of "prune" 
#If the word is not in code vocabulary print ({word} is not in my memory)
#The user will select the would translate to

dictionary = {
    "prune" : "élaguer",
    "school":"école",
    "market" : "marché",
    "house" : "Maison",
    "book" : "Livre",
    "water" : "eau",
    "friend" : "Amie",
    "Mountain": "Montagne",
    "city" : "ville"
}

language = input("What will language will you liake to translate to: ")
# word = input("what word will you like to translate: ")
# my_word = dictionary.get(word)

if language == 'french':
    word = input("what word will you like to translate: ")
    my_word = dictionary.get(word)
    if my_word:
        print(f"The translation of the word is: {my_word}")
    else:
        print(f"{word} is not in my memory")
else:
    print("Invalid Language selected")