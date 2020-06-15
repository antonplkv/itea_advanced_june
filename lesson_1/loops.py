# start = 0
# end = 100
#
#
# while start < end:
#     start += 1
#
#     if start ** 2 > 16732:
#         break
#
#     if start % 2:
#         continue
#     print(start ** 2)
# else:
#     print('Ended without break block')


my_list = [1, 2, 3, 4, 5, 6, 8, 9]

products = {
    'cherry': 110,
    'strawberry': 100,
    'cucumber': 40
}


for name, price in products.items():
    print(name, price)

inputs = ''


print('c' in ['a', 'b'])

for i in range(10):
    result = input('Enter value')
    inputs += result