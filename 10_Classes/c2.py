from c1 import Car


class SportCar(Car):
    def __init__(self):
        super().__init__()


s1 = SportCar()
print(s1.year)
