from telegram.ext import Updater, CommandHandler, InlineQueryHandler, MessageHandler
from time import sleep
import schedule

MY_TOKEN_ID = "5770561614:AAFuGC5eut7RwOf7UNi7_eglCVAnGjTESis"
MY_GROUP_ID = '-682460728'
updater = Updater(MY_TOKEN_ID)


def sendMessage():
    updater.bot.send_message(MY_GROUP_ID, "Olá")

# Define os horários do dia que serão mandadas a mensagem
# schedule.every().day.at("06:00").do(sendMessage)
# schedule.every().day.at("12:00").do(sendMessage)
# schedule.every().day.at("18:00").do(sendMessage)
# schedule.every().to(6).hours.do(sendMessage)
schedule.every(30).seconds.do(sendMessage)

def main():
    updater.start_polling()

    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == "__main__":
    main()