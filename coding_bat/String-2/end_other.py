def end_other(a, b):
    a = a.lower()
    b = b.lower()

    larger = a
    if len(b) > len(a):
        larger = b

    if larger == a:
        return a[(len(a) - len(b)):] == b
    else:
        return b[(len(b) - len(a)):] == a


print(end_other('Hiabc', 'bc'))
