import telepot
token = 'Api_Key_from_botfather'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe()) #it gives you metadata

print(TelegramBot.getUpdates()) #it gives you updates of your bot



