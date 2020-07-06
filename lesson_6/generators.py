def my_range(start, stop, end=1):

    while start < stop:
        value = start
        start += 1
        yield value
        print('Unfrozen')
        yield 1000


generator_iterator = iter(my_range(0, 3))

print(next(generator_iterator))
print(next(generator_iterator))
print(next(generator_iterator))
print(next(generator_iterator))
print(next(generator_iterator))
print(next(generator_iterator))