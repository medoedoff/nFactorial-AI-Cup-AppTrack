from settings import teleBot
from flask import Blueprint
from models import CohereClassification

@teleBot.message_handler(commands=["start"])
def sendMessage(message):
    teleBot.send_message(message.chat.id, "Greetings! Send me your suspicious message")

@teleBot.message_handler(func=lambda message: True)
def messageFromUser(message):
    cohereClassification = CohereClassification(message=message.text)
    response = cohereClassification.get()
    print(response)
    teleBot.reply_to(message, response)

# Convert the handlers instance to a Flask blueprint
handlers = Blueprint("handlers", __name__)