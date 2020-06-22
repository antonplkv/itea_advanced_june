import random


def repeater(repeats):

    def decorator(func):

        def wrapper(*args):
            results = []
            print('Functions is wrapping')

            for i in range(repeats):
                results.append(func(*args))

            print('Function is wrapped')
            return results
        return wrapper
    return decorator


@repeater(23)
def get_random(min_, max_):
    return random.randint(min_, max_)


@repeater(30)
def get_pi():
    return 3.1415


#print(repeater(30)(get_random)(10, 300))