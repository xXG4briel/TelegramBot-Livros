import telebot, time, datetime

FILE = open("info.txt", "r").readlines() # Abre um arquivo txt
TOKEN = FILE[0].replace("\n","") # Pega o primeiro index
GROUP_ID = FILE[1].replace("\n","") # Pega o segundo index

hoursSend = []
messagesSendInDay = 0
bot = telebot.TeleBot(TOKEN)

while True:
    hoje = datetime.datetime.today()
    bot.send_message(GROUP_ID, hoje)
    # try:
    #     bot.send_message(GROUP_ID, hoje)
    # except Exception as ex:
    #     print(ex)
    time.sleep(1)
    # try:
    #     from datetime import datetime

    #     now = datetime.date.today() # datetime.now()
    #     # Pega o hórario atual
    #     currentTime = now.strftime("%H:%M") #00:00
    #     currentTimeHour = int(currentTime[0:2])
    #     currentTimeMinutes = int(currentTime[3:5])

    #     hoursToSend = [6, 12, 18]

    #     # hour = input("HOUR: ")

    #     # Verifica se a mensagem já foi enviada
    #     # Verificase se a mensagem está na lista de horários para enviar
    #     if currentTimeHour not in hoursSend and currentTimeHour in hoursToSend :

    #         bot.send_message(GROUP_ID, currentTimeHour) # Manda a mensagem para o grupo escolhido
            
    #         messagesSendInDay += 1
    #         hoursSend.append(currentTimeHour)

    #         indexHour = hoursToSend.index(currentTimeHour)

    #         HOURS = 0

    #         # Pega o próximo horário - o horário inserido
    #         if currentTimeHour == 6 or currentTimeHour == 12:
    #             HOURS = hoursSend[indexHour + 1] - currentTimeHour
    #         else:  # Se for 18
    #             # horário do dia - horário atual - proximo horário
    #             HOURS = 24 - currentTimeHour + 6

    #         # Converte as horas para minuto e subtrai os minutos inseridos
    #         MINUTES = (HOURS * 60) - currentTimeMinutes
    #         # Converter os minutos para segundos
    #         SECONDS = MINUTES * 60


    #         if messagesSendInDay == 3: # Verifica se já foi mandado 3 mensagens
    #             messagesSendInDay = 0 # zera pois só será enviada a mensagem no dia seguinte
    #             hoursSend.clear() # limpa a lista

    #         time.sleep(SECONDS)    

    # except Exception as ex:
    #     print('[x] error: ', ex)
    
bot.polling(none_stop=True)
    # bot.polling()