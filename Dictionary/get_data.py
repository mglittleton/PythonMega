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
            close = get_close_matches(word, words, 4, 0.5)
            if not close:
                close = ["<error>"]
            print("That word does not exist.")
            print("Did you mean: ")

            for i in range(0, len(close)):
                print('{0}. {1}'.format(i + 1, close[i]))
            print("X. NONE of the above")
            close_choice = input('Please type the number of the closest match: ')

            if close_choice == 'x' or close_choice == "X":
                print('----------------------------------------')
                print('Please try entering the word again.')
                word = ''
                continue
            word = close[int(close_choice) - 1]

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


