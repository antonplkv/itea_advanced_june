list_of_elements = [1, 2, 3, 4]
print(list_of_elements[0])


def test(a, b, c):
    pass


test(b=100, a=200, c=300)

a = 100


def get_the_value():
    pass


class Phone:

    def __init__(self, model):
        self._model = model

    def get_model(self):
        return self._model

    def is_iphone(self):
        return self._model == 'Apple'
