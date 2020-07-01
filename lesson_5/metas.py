#a = [1, 2, 3]

#
# class Car:
#
#     vehicle_type = 'Truck'
#
#     def beep(self):
#         print('Beep')
#
#
# def beep(self):
#     print('Beep')
#
#
# MyClass = type('Car', (), {'vehicle_type': 'Truck', 'beep': beep})
#
# car = MyClass()
#
# print(car.vehicle_type)
# print(car.beep())


class MyMetaClass(type):

    black_list_name = 'get_b'

    def __new__(cls, name, base, attrs):
        print(cls, name, base, attrs)
        name = 'CreatedByMetaclass' + name
        attrs.update({'created_by': MyMetaClass})
        if MyMetaClass.black_list_name in attrs:
            raise ValueError(f'You cannot name your methods as {MyMetaClass.black_list_name}')
        return super().__new__(cls, name, base, attrs)


class MyClass(metaclass=MyMetaClass):

    def __init__(self, a):
        self._a = a

    def get_a(self):
        return self._a

obj = MyClass(1)

print(MyClass.__name__)