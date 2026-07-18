# Enter the English message to translate into Pig Latin:

# My name is AL SWEIGART and I am 4, 000 years old.

# Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4, 000 yearsyay oldyay.


# 'a', 'e', 'i', 'o', 'u', 'y'

# starts with vowel -> add 'yay' to the end of the word.

# consonant or consonant cluster -> move that consonant word to the end and the add 'ay'


# print('Enter the English message to translate into Pig Latin:')

user_text = 'My name is AL SWEIGART and I am 4, 000 years old.'
print(user_text)

vowles = ['a', 'e', 'i', 'o', 'u', 'y']

splitted_user_text_list = user_text.split(' ')

# splitted_user_text_list = ['My', 'name', 'is', 'AL', 'SWEIGART', 'and', 'I', 'am', '4,', '000', 'years', 'old.']

# print(splitted_user_text_list)

final_user_text = ''

# captial_word = False

for i in splitted_user_text_list:  # 'My'
    if splitted_user_text_list.index(i) == splitted_user_text_list[len(splitted_user_text_list) - 1]:
        final_user_text = final_user_text + i[:len(i)-1] + 'ay' + i[-1]
    if i[0].isdecimal():
        final_user_text = final_user_text + i + ' '
    elif i[0].lower() in vowles:
        if i.isupper():
            final_user_text = final_user_text + i + 'YAY '
        else:
            final_user_text = final_user_text + i + 'yay '
    else:
        # final_user_text = final_user_text + \
        #     i[1:] + i[0].lower() + 'ay '

        clutser_part = ''
        remaining_part = ''

        lower_word = i.lower()  # sweigart

        for j in range(len(lower_word)):
            if lower_word[j] not in vowles:
                clutser_part = clutser_part + lower_word[j]
            else:
                remaining_part = remaining_part + lower_word[j:]
                break

        if i.isupper():
            final_user_text = final_user_text + \
                remaining_part.upper() + clutser_part.upper() + 'AY '
        else:
            final_user_text = final_user_text + remaining_part + clutser_part + 'ay '

print(final_user_text)
