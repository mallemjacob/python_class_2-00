# Inheritance

# parents to children

# assets
# behaviours

# Parent class
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.odometer = 0
        self.age = 19

    def info(self):
        return f"The cat maker is {self.name}. The model is {self.model}. It is made in the year {self.year}."


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


# b1 = Battery(80)
# b1.battery_size


class ElectricCar(Car):
    def __init__(self, name, model, year, battery_cap):
        super().__init__(name, model, year)
        self.engine = "Electric"
        # Instances as Attributes
        self.battery = Battery(battery_cap)

    def info(self):
        return f"The manufacturer is {self.name}. The car model is {self.model}. The odomter is {self.odometer}"


e1 = ElectricCar('nissan', "B420", 2026, 90)
e2 = ElectricCar('telsa', "A21", 2025, 100)

print(e1.name)
print(e1.model)
print(e1.year)

print(e1.info())

print(e1.engine)

print(e1.battery.battery_size)
print(e2.battery.battery_size)

e1.battery.describe_battery()
e2.battery.describe_battery()

# parent - child
# car - ElectricCar, sportcar
# Human -> Indian -> South Indian, North India
# Languages - English, FRench, German


# Write age = 19 as attribute is car class
