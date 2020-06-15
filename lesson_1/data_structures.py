list_of_numbers = [1, 3, 5, 7, 9]

r = list_of_numbers[3]
print(r)

list_of_numbers[3] = 77
print(list_of_numbers)

new_list = list([1, 2, 3, 4, 5])
print(new_list)

#(int, str, float, tuple,) => (*)
products = {
    'cherry': 110,
    'strawberry': 100,
    'cucumber': 40
}

birthdays = {
    (23, 2): 'Max',
    (20, 5): 'Andrew'
}

tomato_price = products.get('cucumber', 0)
print(tomato_price)

print(birthdays.get((20, 5), 'Nobody'))

print(products.items())


products.update({'cherry': 130, 'cucumber': 35})

print(products)


list_of_numbers = (1, 3, 5, 7, 9)

taxi_park = {'toyota', 'toyota', 'toyota', 'mercedes', 'hyundai', 'hyundai'}
taxi_park2 = {'nissan', 'nissan', 'BMW', 'hyundai'}

print(taxi_park)
taxi_park2.discard('nissan')
print(taxi_park2)

print(taxi_park | taxi_park2)
print(taxi_park & taxi_park2)