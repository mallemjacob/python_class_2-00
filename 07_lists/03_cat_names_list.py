"""Lesson 16: building a list from user input."""


def collect_cat_names():
    cat_list = []

    while True:
        cat_name = input('Enter the cat name: ')

        if cat_name == '':
            break

        if cat_name in cat_list:
            print('That cat name already exists. Try another one.')
        else:
            cat_list = cat_list + [cat_name]

    return cat_list


if __name__ == '__main__':
    print(collect_cat_names())
