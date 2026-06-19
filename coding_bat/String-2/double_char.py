# name = 'mouse'

# new_str = ''  # mm
# for i in name:
#     new_str = new_str + (i * 2)

# print(new_str)

# Given a string, return a string where for every char in the original, there are two chars.


def double_char(str):
    new_str = ''
    for i in str:
        new_str = new_str + (i * 2)

    return new_str


double_char('The')
double_char('AAbb')
double_char('Hi-There')
