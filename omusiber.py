try:
	import telepot
except(ImportError):
	import os
	os.system('sudo pip3 install telepot')
import env

token = env.token
chat_id = env.chat_id

bot = telepot.Bot(token)
bot.sendMessage(chat_id,"testt")
