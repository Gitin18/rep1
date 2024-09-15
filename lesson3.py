


import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

API_TOKEN = "7241789327:AAHh7ar-BDR9lN4rKAbnhdFfWNZ55Zm38bQ"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_button = KeyboardButton(
        text="Открыть генератор паролей",
        web_app=WebAppInfo(url="https://your-repl-name.your-username.repl.co/set_user/{}".format(message.chat.id))
    )
    markup.add(web_app_button)
    bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы открыть генератор паролей:", reply_markup=markup)

bot.polling(non_stop=True)
