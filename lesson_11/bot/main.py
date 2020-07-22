from telebot import TeleBot
from .config import TOKEN

bot = TeleBot(TOKEN)


@bot.message_handler(content_types=['text'], commands=['start'])
def start(message):
    print(message.text)
    bot.send_message(message.from_user.id, 'Здравствуйте!')


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)