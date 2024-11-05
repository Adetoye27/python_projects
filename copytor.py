'''
write a function called copy, which takes in a file name and a new file name and copies the content of the file into the second file 
(Note: We've provided you with the first chapter of Alice's Adventure in Wonderland to give you some sample text to work with. this is also the text used in the tests)
copy('story.txt', 'story_copy.txt') #None
#expect the contents of the 'story.txt' and 'story_copy.txt' to be same

'''

def copy(first_file, second_file):
    with open(first_file, 'r') as first_file:
        content = first_file.read()
    with open(second_file, 'w') as second_file:
        second_file.write(content)

copy('story.txt', 'story_copy.txt')



