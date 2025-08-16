import telepot
token = 'Api_Key_from_botfather'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())

print(TelegramBot.getUpdates())

