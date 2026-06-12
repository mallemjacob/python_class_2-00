"""Lesson 5: while loops, for loops, break, and continue."""


count = 1

while count <= 10:
    if count == 5:
        break
    print(count)
    count = count + 1

print('the end')

for number in range(1, 11):
    if 4 <= number <= 6:
        continue
    print(number)

for number in range(0, 11, 3):
    print(number)
