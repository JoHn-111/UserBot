from pyrogram.types import Message
from pyrogram import filters
from utils import app
import time


@app.on_message(filters.command('manul', ['.']))
def manul(client, message):
	quantity = message.command[1]
	quantity = int(quantity) + 1
	print('manul')
	message.delete()
	for i in range(1, quantity):
		client.send_message(message.chat.id, f"{i} манула(ов)")
		time.sleep(0.2)
