OUTPUT = 'summary.txt'
WRITE_MODE = 'w'
FILENAME = 'book.txt'
READ_MODE = 'r'

with open(OUTPUT, WRITE_MODE) as output:
    #function to summarize letters 
    def summarize_letters(string):
        characters = []
        for word in string.upper().split():
            characters.extend(list(word))
        
        character_counts = {}

        for character in characters:
            if character in character_counts: 
                character_counts[character] += 1  # update existing key-value pair
            else:
                character_counts[character] = 1  # insert new key-value pair
            
        for character, count in sorted(character_counts.items()):
            output.write(f'{character:<2}{count}\n')
        
        if len(characters) == 26:
            output.write('It has all letters.\n')
        else:
            output.write('It does not have all letters.\n')
    #read the txt file and run function
    with open(FILENAME, READ_MODE) as book:
        data = book.read()

        summarize_letters(data)

    # check if all letters of the alphabet are in the book.txt
    
