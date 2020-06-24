class AlreadyExists(Exception):
    pass


class Singletone:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            raise AlreadyExists

        obj = super().__new__(cls)
        cls._instance = obj
        return obj

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


singleton1 = Singletone('name')
singleton2 = Singletone('name2')
singleton3 = Singletone('name3')

print(singleton1.get_name(), singleton2.get_name(), singleton3.get_name())