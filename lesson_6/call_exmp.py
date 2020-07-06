class ExampleClass:

    def __init__(self, a):
        self._a = a

    def __call__(self, *args, **kwargs):
        print(f'Object of class {self.__class__.__name__} was called')


class Decorator:

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print('Start decorating')
        result = self.fn(*args, **kwargs)
        print('End decorating')
        return result


@Decorator
def target_function(arg1):
    print(arg1)
    return arg1


print(target_function(10))

