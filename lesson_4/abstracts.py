from abc import ABC, abstractmethod


class WrongColourError(Exception):
    pass


class AbstractCar(ABC):

    AVAILABLE_COLOURS = ('Yellow', 'Black', 'White')

    def __init__(self, colour, engine):
        self._colour = colour
        self._engine = engine

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        if value in AbstractCar.AVAILABLE_COLOURS:
            self._colour = value
        else:
            raise WrongColourError(f'Available colours are {AbstractCar.AVAILABLE_COLOURS}')

    @colour.deleter
    def colour(self):
        self._colour = None

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value

    @abstractmethod
    def drive(self):
        print(f'My light car of {self._colour} colour is driving')

    @abstractmethod
    def open_door(self):
        pass


class Car(AbstractCar):

    def drive(self):
        super().drive()

    def open_door(self):
        print('Opening the doors')


car = Car('black', 'v-6')
car.drive()
car.open_door()


car.colour = 'Black'
print(car.colour)

print(car.engine)

car.engine = 'V-8'
print(car.engine)



class Car:

    def __init__(self, colour, engine):
        self._colour = colour
        self._engine = engine

    def get_colour(self):
        return self._colour

    def set_colour(self, value):
        if value in AbstractCar.AVAILABLE_COLOURS:
            self._colour = value
        else:
            raise WrongColourError(f'Available colours are {AbstractCar.AVAILABLE_COLOURS}')

    colour = property(get_colour, set_colour)

    def get_engine(self):
        return self._engine

    def set_engine(self, value):
        self._engine = value

    def del_engine(self):
        self._engine = None

    engine = property(get_engine, set_engine, del_engine)


car = Car('White', 'V-6')
print(car.colour)
car.colour = 'Black'
print(car.colour)

print(car.engine)
car.engine = 'V-8'
print(car.engine)

del car.engine
print(car.engine)