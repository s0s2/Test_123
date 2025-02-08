import telebot

import logging
from random import random_karpov

from reply_david import replyd
from telebot import types

from inline_Rom import f
from inline_Rom import s

from tex_Belyak import Belyak


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot = telebot.TeleBot("7512750009:AAHYQt5qndrJLjeUEHcl2IRwwDWakmgcm-A", parse_mode=None)
admins = []
visitors = []

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    if message.chat.id in admins:
        bot.send_message(message.chat.id, "/new_text - создать новое сообщение для рассылки \n"
                                          "/new_link - создать ссылку для рассылки \n"
                                          "/send - для отправки рассылки")
    else:
        bot.send_message(message.chat.id, "Привет!")


@bot.message_handler(commands=['new_text'])
def new_text(message):
    bot.send_message(message.chat.id, "Введите текст для рассылки.")

@bot.message_handler(commands=['new_link'])
def new_link(message):
    bot.send_message(message.chat.id, "Введите ссылку для рассылки.")

@bot.message_handler(commands=['send'])
def send(message):
    bot.send_message(message.chat.id, "Рассылка успешно отправлена.")



@bot.message_handler(commands=['random'])
def send(message):
    random_karpov(message, bot, types)

@bot.message_handler(commands=['replyd'])
def repla(message):
    replyd(message, bot, types)



@bot.message_handler(commands=['s'])
def s(message):
    bot.send_message(message.chat.id, "Нажми плз ♡")

@bot.message_handler(commands=['f'])
def f(message):
    bot.send_message(message.chat.id, "Оцени плз ♡")

@bot.message_handler(commands=['g'])
def g(message):
    bot.send_message(message.chat.id, "Тренируйся плз ♡")

@bot.message_handler(commands=['Belyak'])
def bel(message):
    Belyak(message, bot)




bot.infinity_polling()