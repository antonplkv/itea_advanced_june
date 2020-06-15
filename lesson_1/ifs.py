# import random
#
# rn = random.randint(0, 100)

rain = 'No rain'
sun = 'Shines bright'
temperature = 'warm'


if all([rain == 'No rain', sun == 'Shines bright', temperature == 'warm']):
    print('The weather is nice')
else:
    print('Something wrong with weather')


temperature = 13


# if temperature > 12:
#     message = 'Warm'
# else:
#     message = 'Cold'

message = 'Warm' if temperature > 12 else 'Cold'
print(message)