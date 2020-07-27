from models import Car

cars = ['VW', 'BMW', 'MERCEDES', 'LAMBORGHINI', 'AUDI']
CAR_IMAGE = 'car.jpeg'


def seed_cars(photo_path):
    for car in cars:

        with open(photo_path, 'rb') as car_file:
            car_obj = Car.objects.create(title=car)
            car_obj.photo.put(car_file, content_type='image/jpeg')
            car_obj.save()


if __name__ == '__main__':
    Car.objects.delete()
    seed_cars(CAR_IMAGE)