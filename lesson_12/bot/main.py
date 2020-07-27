from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from .config import TOKEN, SEPARATOR
from .texts import GREETINGS, CHOOSE_CAR
from .keyboards import START_KB

from .db.models import Car

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(*[KeyboardButton(button) for button in START_KB.values()])
    bot.send_message(message.chat.id, GREETINGS, reply_markup=kb)

"LOOKUP('class name') + SEPARATOR + {OBJECT_ID}"

@bot.message_handler(func=lambda m: m.text == START_KB['list_of_cars'])
def list_of_cars(message):
    kb = InlineKeyboardMarkup()

    cars = [
        InlineKeyboardButton(
            car.title,
            callback_data=f'{Car.__name__}{SEPARATOR}{car.id}'
        ) for car in Car.objects
    ]

    kb.add(*cars)

    bot.send_message(message.chat.id, CHOOSE_CAR, reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data.split(SEPARATOR)[0] == Car.__name__)
def clicked_car(call):
    car_id = call.data.split(SEPARATOR)[1]
    car_obj = Car.objects.get(id=car_id)
    bot.send_photo(call.message.chat.id, car_obj.photo.read(), caption=car_obj.title)


@bot.message_handler(func=lambda m: True)
def any_message(message):
    bot.send_message(message.chat.id, message.text[::-1])