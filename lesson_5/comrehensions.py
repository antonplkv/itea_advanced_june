squares = []

for i in range(0, 10):
    squares.append(i ** 2)

print(squares)

compr_squares = [i ** 3 if i % 2 == 0 else i ** 2 for i in range(10)]
print(compr_squares)

compr_dict = {i: i ** 2 for i in range(10)}
print(compr_dict)

compr_set = {i for i in range(10)}
print(compr_set)

exmp = (i for i in range(10))
