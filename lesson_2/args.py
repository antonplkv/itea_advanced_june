def my_sum(*args):
    result = 0
    for number in args:
        result += number
    return result


arguments = [1, 2, 100, 300, 400, 1000, 213]
arguments2 = [400, 500, 600]
r = my_sum(*arguments, *arguments2, 300, 400, 13)
print(r)


def my_mult(a, b, c):
    return a * b * c

result = [4, 5, 6]

print(my_mult(*result))


def my_func(*args, **kwargs):
    print(args)
    print(kwargs)

'eqweqw'.isdigit()


def elems(*args):
    pass

my_func(10, 20, 30, 40, a=1, bq=2, zxc=3, cv=441, qw=2)