pig = 'ay'

OGword = input('Please enter a word: ')
if len(OGword) > 0 and OGword.isalpha():
        first_letter = OGword[0]
        rest = OGword[1:]
        new_word = rest + first_letter + pig
        print('This is your translated word: ', (new_word))
else:
        print('That\'s not a valid word!')

        
