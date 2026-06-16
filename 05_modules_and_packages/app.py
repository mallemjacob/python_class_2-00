# modules

# user-defined modules
import good_morning  # user-defined module
import random  # build-in module


def random_number_generator():
    random_number = random.randint(1, 3)
    response = good_morning.greeter(random_number)
    return response


print(random_number_generator())
