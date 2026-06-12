"""Lesson 3: reading user input and converting types."""


def get_grade(marks):
    if 35 <= marks <= 50:
        return 'grade C'
    if 50 < marks <= 75:
        return 'grade B'
    if 75 < marks <= 100:
        return 'grade A'
    return 'invalid marks'


def main():
    name = input('Enter your name: ')

    if name == 'mouse':
        print('Your name matches.')
    else:
        print('Wrong name.')

    student_marks = int(input('Enter your marks: '))
    print(get_grade(student_marks))


if __name__ == '__main__':
    main()
