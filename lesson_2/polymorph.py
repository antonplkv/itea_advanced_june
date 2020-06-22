class Balloon:

    def __init__(self, size, colour):
        self._size = size
        self._colour = colour

    def get_size(self):
        return self._size

    def set_size(self, value):
        self._size = value

    def get_colour(self):
        return self._colour

    def set_colour(self, value):
        self._colour = value

    def fly(self):
        print(f'The baloon of {self._colour} is flying')

    def __add__(self, other):
        size = self._size + other.get_size()
        colour = self._colour + '-' + other.get_colour()
        return Balloon(size, colour)

    def __str__(self):
        return f'Size is {self._size} and colour is {self._colour}'


balloon = Balloon(10, 'red')
balloon1 = Balloon(15, 'green')
balloon2 = Balloon(20, 'blue')
balloon.fly()
balloon1.fly()
balloon2.fly()
print(balloon1)

new_balloon = balloon + balloon1 + balloon2
print(new_balloon)


class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b


class B(A):

    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c


obj = B(1, 2, 3)
print(obj.c)