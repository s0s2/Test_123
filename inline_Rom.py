def f(message, bot, types):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="xxx", url="https://steamcommunity.com/profiles/76561198855309832/"))
    bot.send_message(f, message, reply_markup=markup)

def g(message, bot, types):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(message="lll", url="https://kompege.ru/task"))
    bot.send_message(g, message, reply_markup=markup)

def s(message, bot, types):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(message="zxc", url="https://steamcommunity.com/profiles/76561198855309832/tradeoffers/"))
    bot.send_message(g, message, reply_markup=markup)

