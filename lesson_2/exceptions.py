print('Hello')


# try:
#     a = int(input('ENter a'))
#     b = int(input('Enter b'))
# except ValueError:
#     a = 0
#     b = 1
#
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print('You cant divide by zero!')
#
# print('world')



# try:
#     '123' + 123
#     1 / 0
# except (TypeError, ZeroDivisionError) as err:
#     print('Type and math exceptions')
# except (AttributeError, IndexError) as err:
#     print('Attribute and index error')

try:
    file = open('hello_fil1e', 'r')
except FileNotFoundError:
    print('Не удалось открыть файл')
else:
    print('Работа с файлом произведена успешно')
finally:
    try:
        file.close()
    except NameError:
        print('Файл даже не открывался')
    print('Работа с файлом окончена')
