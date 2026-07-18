# Human -> Indian -> South Indian, North India


class Human:
    def __init__(self):
        self.species = "Homo sapiens"
        self.year = "1 million"


class Indian(Human):
    def __init__(self):
        super().__init__()
        self.region = "12.34, 45.35"


class SouthIndian(Indian):
    def __init__(self):
        super().__init__()


s1 = SouthIndian()

print(s1.species)
