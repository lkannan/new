import sys

import requests

print(sys.executable)

r = requests.get("https://www.google.com/")
print(r.status_code)

print(sys.version)
print("hi")

'''this is a temp doc string'''


class Car:
    def __init__(self, color):
        super().__init__()
        self.color = color


my_car = Car("blue")


def crash(car1, car2):
    car1.color = "burnt"


crash(Car("red"), my_car)
mynewCar = my_car
