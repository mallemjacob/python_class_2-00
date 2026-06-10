# Ask user for cat name
# If the cat alredy exists, tell them to give a new name
# If they enter without cat name, exit the program

cat_list = []

while True:
    cat_name = input('Enter the cat name: ')  # snoopy
    if cat_name == '':
        break
    if cat_name in cat_list:
        print('Already that cat name exists. Try another one.')
    else:
        cat_list = cat_list + [cat_name]

print(cat_list)
