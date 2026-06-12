"""Lesson 4: if, elif, else, and boolean operators."""


def can_get_id(age, state, has_driving_license):
    return age > 18 and state == 'AP' and has_driving_license


def greeting_for_hour(hour):
    if hour < 10:
        return 'Good morning'
    if hour < 16:
        return 'Good afternoon'
    if hour < 20:
        return 'Good evening'
    return 'Good night'


def can_join_class(student_time, class_time, homework_completed):
    return student_time < class_time or homework_completed


print(can_get_id(20, 'AP', True))
print(greeting_for_hour(15))
print(can_join_class(12, 10, True))
