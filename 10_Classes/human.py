class Human:
    def __init__(self, name, age, location):
        # Attributes
        self.name = name
        self.age = age
        self.location = location
        self.intelligent = True

    # Methods
    def speak(self):
        return "Hello"

    def updateName(self, name):
        if name == "admin":
            self.name = name


person1 = Human('Jacob', 30, 'Guntur')  # instance

# Reading attributes
print(person1.name)
print(person1.age)
print(person1.location)
print(person1.intelligent)

# Changing attributes
person1.updateName('Manu')

print(person1.name)

print(person1.speak())


# fruits = ['apples', 'oranges']

# fruits.append()


# class List:
#     def __init__(self, lenght):
#         self.lenght = lenght

#     def append():
#         //some code

#     def extend():
#         //some code


# dic = {}
# dic.keys()
