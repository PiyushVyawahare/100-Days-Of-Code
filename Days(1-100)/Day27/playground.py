# Playing with *args (Many Positional Arguments)
# and *kwargs (Many Keyword arguments)

def add(*args):
    ans = 0
    for i in args:
        ans += i
    print(ans)


add(1, 2, 3, 4, 5, 6, 7)


def calculate(n, **kwargs):
    print(kwargs)
    # for k, v in kwargs.items():
    #     print(k)
    #     print(v)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(5, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
