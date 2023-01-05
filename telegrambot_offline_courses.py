import json
import telebot
from telebot import types
from test import *

URL = 'https://www.google.com/maps/search/%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BA%D1%83%D1%80%D1%81%D1%8B+%D0%B2+%D0%91%D0%B8%D1%88%D0%BA%D0%B5%D0%BA%D0%B5/@42.8760111,74.5856421,14z/data=!3m1!4b1'

bot = telebot.TeleBot('5876023372:AAHBK5lmPJ-wPxsV3dgE0b6Kqcpr5uxa6UM')
choice = types.InlineKeyboardMarkup()
button = types.InlineKeyboardButton('Courses', callback_data='courses')
choice.add(button)

html = get_courses(url=URL)
soup = get_soup(html)
data = get_data(soup)


@bot.message_handler(commands=['start'])
def star_message(message):
    bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(commands=['offline'])
def get_offline_courses(message):
    for i in data:
        bot.send_message(message.chat.id, i)


bot.polling()
