"""Challenge 340"""

USER_INPUT = input('Input string of alphabetical characters :')

if not USER_INPUT.isalpha():
    raise ValueError('input does not only contain alphabetical characters')

MEME_CACHE = []
for index, c in enumerate(USER_INPUT):
    if c in MEME_CACHE:
        print(c + ' is a reccuring character at index ' + str(index))
    else:
        MEME_CACHE.append(c)

print('end')
