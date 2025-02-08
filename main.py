import telebot
import logging

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



bot.infinity_polling()