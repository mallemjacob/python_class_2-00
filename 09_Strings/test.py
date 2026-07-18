vowles = ['a', 'e', 'i', 'o', 'u', 'y']


word = 'name'

clutser_part = ''
remaining_part = ''

lower_word = word.lower()  # sweigart

for i in range(len(lower_word)):
    if lower_word[i] not in vowles:
        clutser_part = clutser_part + lower_word[i]
    else:
        remaining_part = remaining_part + lower_word[i:]
        break


# print(clutser_part)

# print(remaining_part)

if word.isupper():
    print(remaining_part.upper() + clutser_part.upper() + 'AY')
else:
    print(remaining_part + clutser_part + 'ay')
