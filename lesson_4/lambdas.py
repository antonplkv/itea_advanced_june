# def confirm_function(func, arg):
#     return func(arg)
#
#
# print(confirm_function(lambda num: num ** 2, 100))


result = map(lambda num1, num2: (num1 ** 2, num2 ** 2), [1, 2, 3, 4, 5, 6], [10, 20, 30, 40, 60, 70])


filter_result = filter(lambda number: number > 100,
                       [10, 200, 101, 302, 16,
                        'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'])
print(list(filter_result))