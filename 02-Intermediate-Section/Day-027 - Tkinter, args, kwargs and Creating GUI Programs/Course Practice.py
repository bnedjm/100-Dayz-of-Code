def add(*args):
    # sum_ = 0
    # for n in args:
    #     sum_+=n

    # return sum_
    sum_ = sum(n for n in args)
    return sum_

# print(add(4,3,2,1,6))

def calculate(n, **kwargs):
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(f"{key} : {value}")
    n+= kwargs['add']
    n*= kwargs['multi']

    print(n)

# calculate(2, add=4, multi=5)

class Car:

    def __init__(self, **kw):
        # self.make = kw['make']
        # self.model = kw['model']
        # get() makes the kwargs optional
        self.make = kw.get('make')
        self.model = kw.get('model')

# my_car = Car(make='Nissan', model='GT-R')
my_car = Car(make='Nissan')
print(my_car.model)
