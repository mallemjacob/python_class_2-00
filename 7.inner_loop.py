switch = False

for i in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
    for j in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
        if i == 5 and j == 5:
            print(i, j)
            switch = True
            break
        else:
            print(i, j)
    if switch:
        break
