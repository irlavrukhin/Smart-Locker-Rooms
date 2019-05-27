import telebot

bot = telebot.TeleBot("824893382:AAGAHUY0jp0y-t2sUX3O4ZHOQd3FUaHaUQQ")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True)
