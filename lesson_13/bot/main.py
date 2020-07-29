from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from .config import TOKEN

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    buttons = [InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(10)]
    kb.add(*buttons)
    bot.send_message(message.chat.id, 'Hello', reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def square(call):
    bot.edit_message_text(int(call.data) ** 2, call.message.chat.id, call.message.message_id)