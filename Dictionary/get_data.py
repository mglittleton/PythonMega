import json
from difflib import get_close_matches

data = json.load(open('data.json'))
word = ''
words = list(data)
running = True


def get_word(st):
    if st in data:
        return data[st]
    else:
        return 0


while running:

    print('----------------------------------------')
    print('What word would you like to search for? ')

    while word == '':
        word = input().lower()
        if word not in data:
            close = get_close_matches(word, words)
            if not close:
                close = ["<error>"]
            print("That word does not exist.")
            print("Did you mean {}.".format(close[0]))
            affirm = input("(Y)es or (N)o - ")
            if affirm == 'n' or affirm == "N":
                print('----------------------------------------')
                print('Please try entering the word again.')
                word = ''
                continue
            word = close[0]

        counter = 0
        print('----------------------------------------')
        print("{} - ".format(word))
        for definition in data[word]:
            counter += 1
            print("{0}. {1}".format(counter, definition))

    print("Would you like to search for something else?")
    loop = input("(Y)es or (N)o - ")
    if loop == 'n' or loop == 'N':
        running = False
    else:
        word = ''


