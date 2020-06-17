class Phone:

    type_ = 'Wireless connection'

    def __init__(self, model, imei):
        self.model = model
        self.imei = imei

    def call(self, number):
        print('calling to', number)

    def send_message(self, number):
        print('sending message to', number)


class Smartphone(Phone):

    def call(self, number):
        print('Connecting to', number)
        print('Calling to', number)

    def download_application(self, application_name):
        print('Downloading application from play market', application_name)

    def play_music(self, track_name):
        print('playing ', track_name)


phone = Phone('Nokia', '31231231eqweqwe1312')
smartphone = Smartphone('Xiaomi', '312312312123')

phone.call('+380951232123')
smartphone.download_application('youtube')
smartphone.call('+390662313322')
smartphone.send_message('+390662313322')

