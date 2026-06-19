# Input
spam = ['apples', 'bananas', 'tofu', 'cats']

# Expcted output
# 'apples, bananas, tofu, and cats'
# 'apples, bananas, and tofu, cats'

final_string = ''

for i in range(len(spam)):  # 0,1,2,3
    if i == len(spam) - 1:
        final_string = final_string + spam[i]
    elif i == len(spam) - 2:
        final_string = final_string + 'and ' + spam[i] + ', '
    else:
        final_string = final_string + spam[i] + ', '

print(final_string)
