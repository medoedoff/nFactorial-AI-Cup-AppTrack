import telebot
import os

from dotenv import load_dotenv

from flask import Flask
from flask import request

load_dotenv()

apiKey = os.getenv("API_KEY")
webHookHostname = os.getenv("NGROK_HOSTNAME")

teleBot = telebot.TeleBot(apiKey)

app = Flask(__name__)


@teleBot.message_handler(commands=["start"])
def sendMessage(message):
    teleBot.reply_to(message, f"Hello, from there")


@app.route(f"/{apiKey}", methods=["POST"])
def getMessage():
    jsonString = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(jsonString)
    teleBot.process_new_updates([update])
    return "!", 200


@app.route("/", methods=["GET", "HEAD", "POST"])
def webhook():
    teleBot.remove_webhook()
    teleBot.set_webhook(url=f"https://{webHookHostname}/{apiKey}")
    return "!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv('PORT', 6000)))