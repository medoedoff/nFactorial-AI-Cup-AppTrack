from settings import teleBot
from flask import Blueprint

@teleBot.message_handler(commands=["start"])
def sendMessage(message):
    teleBot.send_message(message.chat.id, "Greetings! Send me your suspicious message")



# Convert the tele_bot instance to a Flask blueprint
handlers = Blueprint("handlers", __name__)