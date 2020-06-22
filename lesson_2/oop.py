class Cat:

    family = 'Britain'

    def __init__(self, name, gender, family):
        self.name = name
        self.gender = gender
        self.family = family

    def say_meow(self):
        print('Meeooow!')

    def info(self):
        return self.name, self.gender


Cat.family = 'Сфинкс'
new_cat = Cat('Linda', 'female')
new_cat.name = 'Sendy'
print(new_cat.family)

