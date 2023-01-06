import json

import peewee
import telebot
from telebot import types
from test import *
from info import *

URL = url

bot = telebot.TeleBot(TOKEN)

html = get_courses(url=URL)
soup = get_soup(html)
data = get_data(soup)

courses = peewee.PostgresqlDatabase(
    'team1',
    user=USER,
    password=PASSWORD,
    host='localhost',
    port=5432
)

cursor = courses.cursor()

cursor.execute('SELECT title, status, price FROM courses_course')
results = cursor.fetchall()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Off')
    btn2 = types.KeyboardButton('On')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Hello', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Off':
        for i in data[:5]:
            bot.send_message(message.chat.id, i)
    elif message.text == 'On':
        for k in results[:5]:
            bot.send_message(message.chat.id, k)


bot.polling()
