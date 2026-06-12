"""Lesson 7: nested loops and stopping both loops."""


found_target = False

for row in range(1, 11):
    for column in range(1, 11):
        print(row, column)

        if row == 5 and column == 5:
            found_target = True
            break

    if found_target:
        break
