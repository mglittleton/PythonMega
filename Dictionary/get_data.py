import json

data = json.load(open('data.json'))
word = ''


def get_word(st):
    if st in data:
        return data[st]
    else:
        return 0


print('What word would you like to search for? ')

while word == '':
    word = input()
    print(word)
    break

# TODO: uppercase input
# TODO: loop for endless input
# TODO: loop for multiple searches
