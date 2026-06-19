# Return True if the string "cat" and "dog" appear the same number of times in the given string.


def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for i in range(len(str) - 2):
        if str[i] == 'c' and str[i+1] == 'a' and str[i+2] == 't':
            cat_count = cat_count + 1
        elif str[i] == 'd' and str[i+1] == 'o' and str[i+2] == 'g':
            dog_count = dog_count + 1

    return cat_count == dog_count


cat_dog('catdog')
cat_dog('catcat')
cat_dog('1cat1cadodog')
