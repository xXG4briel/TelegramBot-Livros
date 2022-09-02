from telegram.ext import Updater, CommandHandler, InlineQueryHandler, MessageHandler
import telegram.message
from time import sleep

def main():
    MY_TOKEN_ID = "5770561614:AAFuGC5eut7RwOf7UNi7_eglCVAnGjTESis"
    updater = Updater(MY_TOKEN_ID)
    dp = updater.dispatcher
    # dp.add_handler(CommandHandler("clima", weather))
    # updater.start_polling()

    while True:
        updater.bot.send_message(-682460728, "Olá")
        sleep(1)
    # updater.idle()


def weather(bot, update):
    from datetime import datetime
    chat_id = -682460728 # update.message.chat_id
    message = datetime.today()# str(we.message.text)
    # lst = message.split(" ", 1)
    # location = lst[1]
    bot.send_message(chat_id=chat_id, text=message) # getWeather(location=str(location))
        # sleep(1)
    # while True:

if __name__ == "__main__":
    main()